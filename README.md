# Django IntEnumField

An IntEnumField for Django.


## Features

* Store your multiple-choice options as a smallint (2 bytes) instead of varchar
* Reuse existing IntEnums as choice values
* Integrates well with Django's admin app (display and filter)


## Requirements

* Python 2.7+ or 3.4+
* Django 1.8+
* enum34 library on Python 2.x


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


## Running the tests

1. Run `pip install pytest pytest-django`
2. Run `./setup.py test`


## License

This project is licensed under the MIT license. The full license text is
available in the LICENSE file.
