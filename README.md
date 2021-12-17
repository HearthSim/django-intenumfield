# Django IntEnumField

[![Build Status](https://api.travis-ci.org/HearthSim/django-intenumfield.svg?branch=master)](https://travis-ci.org/HearthSim/django-intenumfield)

An IntEnumField for Django.

## Features

* Store your multiple-choice options as a smallint (2 bytes) instead of varchar
* Reuse existing IntEnums as choice values
* Integrates well with Django's admin app (display and filter)

## Requirements

* Python 3.6+
* Django 2.2+

## Usage

```py
from enum import IntEnum
from django.db import models
from django_intenum import IntEnumField


class Status(IntEnum):
	UNKNOWN = 0
	IN_PROGRESS = 1
	COMPLETED = 2
	ERROR = 3


class Job(models.Model):
	status = IntEnumField(enum=Status)
```

## License

This project is licensed under the MIT license. The full license text is
available in the LICENSE file.
