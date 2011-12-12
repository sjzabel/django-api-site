#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages
    
import os

setup(
    name = "django-api-site",
    version = "0.3",
    url = 'https://github.com/sjzabel/django-api-site',
    download_url = 'https://github.com/sjzabel/django-api-site',
    license = 'BSD',
    description = "Api site is a wrapper on top of piston that provides some utilities for creating an api-site",
    author = 'Stephen J. Zabel',
    author_email = 'sjzabel@gmail.com',
    packages = find_packages(),
    namespace_packages = ['api_site'],
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
