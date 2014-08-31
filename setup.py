#!/usr/bin/env python

from distutils.core import setup
import pytwitch

# Get the long description from the relevant file
with open('DESCRIPTION.rst') as f:
    long_description = f.read()

setup(
    name='pytwitch',
    version=pytwitch.__version__,
    description='PyTwitch - Twitch Integration for Python',
    long_description=long_description,
    url='https://github.com/dhh-hss/pytwitch',
    author='Daniel Hyldebrandt Hemmingsen',
    author_email='daniel.h.Hemmingsen@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    keywords=['twitch', 'api', 'development', 'authentication'],
    packages=['pytwitch'],
    install_requires=['requests']
)