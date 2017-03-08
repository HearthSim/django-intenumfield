#!/usr/bin/env python

import os
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTestCommand(TestCommand):
	def run_tests(self):
		import django
		import pytest
		os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
		django.setup()
		test_args = []
		exit(pytest.main(test_args))


test_requirements = [
	"pytest",
	"pytest-django",
]

setup(
	tests_require=test_requirements,
	cmdclass={"test": PyTestCommand},
)
