#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: setup.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-11-24
"""

from setuptools import setup, find_packages

setup(
    name='ak-vendor',
    version='0.6.3',
    description="Some vendor scripts that we use here at Appknox",
    long_description="All the Vendor/helper files the Appknox relies on",
    url='https://github.com/appknox/vendor',
    author='dhilipsiva',
    author_email='dhilipsiva@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='appknox vendor',
    packages=find_packages(),
    py_modules=['ak_vendor'],
    entry_points='',
    install_requires=[
        "python3-protobuf==2.5.0",
    ],
    extras_require={
        'dev': [''],
        'test': [''],
    },
)
