#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pytwitch',
    version='0.0.2',
    description='PyTwitch - Twitch Integration for Python',
    long_description=open('DESCRIPTION.rst').read(),
    author='Daniel Hyldebrandt Hemmingsen',
    author_email='daniel.h.hemmingsen@gmail.com',
    url='https://github.com/dhh-hss/pytwitch',
    keywords=[
        'twitch',
        'api',
        'development',
        'authentication'
    ],
    install_requires=[
        'requests==2.4.0'
    ],
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Build Tools',
    ],
    zip_safe=False,
)