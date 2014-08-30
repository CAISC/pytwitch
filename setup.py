#!/usr/bin/env python

import pytwitch

packages = ['pytwitch']
requires = ['requests']

here = path.abspath(path.dirname(__file__))

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
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ),
    keywords='twitch api development authentication',
    packages=packages,
    install_requires=requires,
    package_data=None,
    package_dir={'pytwitch': 'pytwitch'},
)