from django.core.exceptions import ValidationError
from django.db.models import SmallIntegerField
from django.forms.widgets import Select
from django.utils.deconstruct import deconstructible


@deconstructible
class IntEnumValidator:
	def __init__(self, enum):
		self.enum = enum

	def __call__(self, value):
		if value not in self.enum._value2member_map_:
			raise ValidationError("%r is not a valid %s" % (value, self.enum.name))

	def __eq__(self, other):
		return isinstance(other, IntEnumValidator) and self.enum == other.enum


class IntEnumSelectWidget(Select):
	def render_options(self, selected_choices):
		selected_choices = [int(k) for k in selected_choices if k]
		return super(IntEnumSelectWidget, self).render_options(selected_choices)


class IntEnumField(SmallIntegerField):
	def __init__(self, *args, **kwargs):
		if "enum" in kwargs:
			# if check required for migrations (apparently)
			self.enum = kwargs.pop("enum")
			kwargs["choices"] = tuple((m.value, m.name) for m in self.enum)
			kwargs["validators"] = [IntEnumValidator(self.enum)]
			if "default" in kwargs:
				kwargs["default"] = int(kwargs["default"])
		super(IntEnumField, self).__init__(*args, **kwargs)

	def from_db_value(self, value, expression, connection, context):
		if value is not None:
			try:
				return self.enum(value)
			except ValueError:
				pass
		return value

	def formfield(self, **kwargs):
		defaults = {"widget": IntEnumSelectWidget}
		defaults.update(kwargs)
		return super(IntEnumField, self).formfield(**defaults)
