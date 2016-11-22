from enum import IntEnum
from django.db import models
from django_intenum import IntEnumField


class TestEnum(IntEnum):
	A = 1
	B = 2
	C = 3
	D = 99


class TestModel(models.Model):
	int_field = IntEnumField(enum=TestEnum)
	null_field = IntEnumField(enum=TestEnum, null=True)
