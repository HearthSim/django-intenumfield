import pkg_resources

from django.core.exceptions import ValidationError
from django.db.models import SmallIntegerField
from django.forms.widgets import Select
from django.utils.deconstruct import deconstructible


__version__ = pkg_resources.require("django-intenumfield")[0].version


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
	def format_value(self, value):
		if value is not None:
			value = int(value)
		return super().format_value(value)


class IntEnumField(SmallIntegerField):
	def __init__(self, *args, enum, **kwargs):
		self.enum = enum
		self._default_validator = IntEnumValidator(self.enum)
		kwargs.setdefault("validators", [self._default_validator])
		if "default" in kwargs:
			kwargs["default"] = int(kwargs["default"])

		super().__init__(*args, **kwargs)

		self.choices = tuple((m.value, m.name) for m in self.enum)

	def deconstruct(self):
		name, path, args, keywords = super().deconstruct()
		keywords["enum"] = self.enum

		if "choices" in keywords:
			del keywords["choices"]

		validators = keywords.get("validators", [])
		try:
			validators.remove(self._default_validator)
		except ValueError:
			pass

		return (name, path, args, keywords)

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
		return super().formfield(**defaults)
