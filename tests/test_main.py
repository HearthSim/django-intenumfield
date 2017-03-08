import pytest
from enum import IntEnum
from .models import SampleEnum, SampleModel


@pytest.mark.django_db
def test_field_value():
	m = SampleModel(int_field=SampleEnum.A)
	m.save()
	assert m.int_field == SampleEnum.A
	assert m.int_field == 1
	assert isinstance(m.int_field, IntEnum)
	assert m.null_field is None

	m.null_field = SampleEnum.B
	m.save()
	assert m.null_field == 2
	assert m.null_field == SampleEnum.B
	assert isinstance(m.null_field, IntEnum)

	m.int_field = 1000
	m.save()
	assert m.int_field == 1000
