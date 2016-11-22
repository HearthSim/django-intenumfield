#!/usr/bin/env python

import django_intenum
from setuptools import setup, find_packages


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
	version=django_intenum.__version__,
	packages=find_packages(),
	author=django_intenum.__author__,
	description="An IntEnumField for Django",
	classifiers=CLASSIFIERS,
	download_url="https://github.com/HearthSim/django-intenumfield/tarball/master",
	license="MIT",
	url="https://github.com/HearthSim/django-intenumfield",
	zip_safe=True,
)
