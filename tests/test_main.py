import enum

import pytest

from django_intenum import IntEnumSelectWidget

from .models import SampleEnum, SampleModel


@pytest.mark.django_db
def test_field_value():
	m = SampleModel(int_field=SampleEnum.A)
	m.save()
	assert m.int_field == SampleEnum.A
	assert m.int_field == 1
	assert isinstance(m.int_field, enum.IntEnum)
	assert m.null_field is None

	m.null_field = SampleEnum.B
	m.save()
	assert m.null_field == 2
	assert m.null_field == SampleEnum.B
	assert isinstance(m.null_field, enum.IntEnum)

	m.int_field = 1000
	m.save()
	assert m.int_field == 1000


def test_intenum_select_widget():
	widget = IntEnumSelectWidget()
	value = SampleEnum.A

	assert widget.format_value(SampleEnum.A) == [str(int(value))]

	context = widget.get_context("foo", value, {})
	assert context["widget"]["value"] == [str(int(value))]


def test_intenum_select_widget_null():
	widget = IntEnumSelectWidget()
	value = None
	context = widget.get_context("foo", value, {})
	assert context["widget"]["value"] == [""]
