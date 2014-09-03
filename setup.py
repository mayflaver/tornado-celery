#!/usr/bin/env python

from setuptools import setup, find_packages

version = "0.1"

setup(
    name="torncelery",
    version=version,
    py_modules=["torncelery"],
    author="Mayflower",
    author_email="fucongwang@gmail.com",
    url="https://github.com/mayflaver/tornado-celery",
    license="MIT",
    packages=find_packages(),
    description="a non-blocking Celery client for Tornado web framework.",
    )
