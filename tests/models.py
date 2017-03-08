from enum import IntEnum
from django.db import models
from django_intenum import IntEnumField


class SampleEnum(IntEnum):
	A = 1
	B = 2
	C = 3
	D = 99


class SampleModel(models.Model):
	int_field = IntEnumField(enum=SampleEnum)
	null_field = IntEnumField(enum=SampleEnum, null=True)
