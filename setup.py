#!/usr/bin/env python

import os
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


__version__ = "1.1"
__author__ = "Jerome Leclanche"
__email__ = "jerome@leclan.ch"


class PyTestCommand(TestCommand):
	def run_tests(self):
		import django
		import pytest
		os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
		django.setup()
		test_args = []
		exit(pytest.main(test_args))


CLASSIFIERS = [
	"Development Status :: 5 - Production/Stable",
	"Environment :: Web Environment",
	"Framework :: Django",
	"Intended Audience :: Developers",
	"License :: OSI Approved :: MIT License",
	"Programming Language :: Python",
	"Programming Language :: Python :: 2.7",
	"Programming Language :: Python :: 3",
	"Programming Language :: Python :: 3.4",
	"Programming Language :: Python :: 3.5",
	"Topic :: Games/Entertainment :: Simulation",
]

setup(
	name="django-intenumfield",
	version=__version__,
	packages=find_packages(),
	author=__author__,
	author_email=__email__,
	description="An IntEnumField for Django",
	classifiers=CLASSIFIERS,
	download_url="https://github.com/HearthSim/django-intenumfield/tarball/master",
	license="MIT",
	url="https://github.com/HearthSim/django-intenumfield",
	zip_safe=True,
	cmdclass={"test": PyTestCommand},
)
