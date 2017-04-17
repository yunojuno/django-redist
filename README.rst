.. image:: https://badge.fury.io/py/django-redist.svg
    :target: https://badge.fury.io/py/django-redist

.. image:: https://travis-ci.org/yunojuno/django-redist.svg
    :target: https://travis-ci.org/yunojuno/django-redist

Django Redist
-------------

A template project for creating redistributable Django app. It contains
the various setup, travis, tox bits and bobs required to set up a project
so that it can be uploaded to PyPI, and run on Travis-CI.

Requirements
============

The most important information here is which versions of Django are
supported. 1.8 is the last LTS version, so where possible it's polite to support 1.8-1.11. Once 2.0 arrives and we go all Py3, this will change.

If you are using anything that precludes 1.8, for example the native Postgres JSONField, then explain here why.

If the project has a any external requirements, put them here along with
any explanatory notes as to why they are required.

Installation
============

This should be boilerplate - use PyPI. Also add here any setup configuration
required to get the package working properly. This section should be the
equivalent of a Quick Start - the minimum required to get the package installed
and working.

Add any details on how to setup ``INSTALLED_APPS``, ``MIDDLEWARE``, urls and
so on.

Settings
========

Any Django settings that are available to the package - their defaults, data
types, and the effect of setting them.

Usage
=====

How to use the package - please include code samples.

Tests
=====

Again, should be boilerplate - use ``tox``.

In addition, any details on how to mock out the package when testing the host
project, if relevant.

Contributing
============

Usual rules apply:

1. Fork the project to your own account
2. Create a branch, fix the issue / add the feature
3. Submit PR

Please take care to follow the coding style - and PEP8.

License
=======

This software is distributed under the MIT license.
