#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name="weeby-challenge-server",
    description="Starter server for the Weeby Challenge.",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "Flask",
    ],
)
