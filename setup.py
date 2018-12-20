#!/usr/bin/env python3

from setuptools import setup

install_requires = [
    'docker',
    'empy',
    'pexpect',
    'requests',
]

kwargs = {
    'name': 'rocker',
    'version': '0.0.1',
    'packages': ['rocker'],
    'package_dir': {'': 'src'},
    'package_data': {'rocker': ['templates/*.em']},
    'entry_points': {
        'console_scripts': [
            'rocker = rocker.cli:main',
	    ]
	},
    'author': 'Tully Foote',
    'author_email': 'tfoote@osrfoundation.org',
    'keywords': ['Docker'],
    'classifiers': [
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License'
    ],
    'description': 'A tool to run docker containers with extras',
    'long_description': 'A tool to run docker containers with extra added like nvidia gui support overlayed.',
    'license': 'Apache',
    'install_requires': install_requires,
}

setup(**kwargs)
