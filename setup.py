# -*- coding: utf-8 -*-
#quickstarted Options:
#
# sqlalchemy: True
# auth:       sqlalchemy
# mako:       True
#
#

#This is just a work-around for a Python2.7 issue causing
#interpreter crash at exit when trying to log an info message.
try:
    import logging
    import multiprocessing
except:
    pass

import sys
py_version = sys.version_info[:2]

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

testpkgs=['WebTest >= 1.2.3',
               'nose',
               'coverage',
               'gearbox'
               ]

setup(
    name='parsidan',
    version='0.1.1-prealpha',
    description='',
    author='',
    author_email='',
    #url='',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=testpkgs,
    package_data={'parsidan': ['i18n/*/LC_MESSAGES/*.mo',
                                 'templates/*/*',
                                 'public/*/*']},
    message_extractors={'parsidan': [
            ('**.py', 'python', None),
            ('templates/**.mak', 'mako', None),
            ('mailing/templates/**.mak', 'mako', None),
            ('public/**', 'ignore', None)],
    },

    entry_points={
        'paste.app_factory': [
            'main = parsidan.config.middleware:make_app'
        ],
        'gearbox.plugins': [
            'turbogears-devtools = tg.devtools'
        ]
    },
    zip_safe=False
)
