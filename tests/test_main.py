import pytest
from enum import IntEnum
from .models import TestEnum, TestModel


@pytest.mark.django_db
def test_field_value():
	m = TestModel(int_field=TestEnum.A)
	m.save()
	assert m.int_field == TestEnum.A
	assert m.int_field == 1
	assert isinstance(m.int_field, IntEnum)
	assert m.null_field is None

	m.null_field = TestEnum.B
	m.save()
	assert m.null_field == 2
	assert m.null_field == TestEnum.B
	assert isinstance(m.null_field, IntEnum)

	m.int_field = 1000
	m.save()
	assert m.int_field == 1000
