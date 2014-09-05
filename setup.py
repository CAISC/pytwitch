#!/usr/bin/env python

from setuptools import setup, find_packages

project = {}
with open('pytwitch/__project__.py') as fp:
    exec(fp.read(), project)

setup(
    name=project['__name__'],
    version=project['__version__'],
    description=project['__description__'],
    long_description=open('README.rst').read(),
    author=project['__author__'],
    author_email=project['__author_email__'],
    url=project['__uri__'],
    keywords=project['__keywords__'],
    install_requires=project['__install_requires__'],
    packages=find_packages(),
    license='MIT',
    zip_safe=False,
    classifiers=project['__classifiers__'],
)