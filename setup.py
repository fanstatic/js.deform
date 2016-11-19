# -*- coding: utf-8 -*-

import os

from setuptools import find_packages
from setuptools import setup

version = '2.0.3'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'deform', 'tests', 'test_deform.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.deform',
    version=version,
    description="Fanstatic packaging of deform",
    long_description=long_description,
    keywords='',
    author='Fanstatic developers',
    author_email='kotti@googlegroups.com',
    url='https://github.com/fanstatic/js.deform',
    license='BSD',
    classifiers=[
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "License :: OSI Approved :: BSD License",
    ],
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=[
        'deform>=2.0.3',
        'fanstatic',
        'js.jquery',
        'js.jquery_form',
        'js.jquery_maskedinput',
        'js.jquery_maskmoney',
        'js.jquery_sortable',
        'js.jquery_timepicker_addon',
        'js.jqueryui',
        'js.modernizr',
        'js.select2',
        'js.tinymce',
        'setuptools',
    ],
    extras_require={
        'testing': [
            'pyramid',
            'pyramid_chameleon',
            'pytest>=3.0.0',
            'pytest-cov',
            'pytest-pep8!=1.0.3',
            'pytest-warnings',
            'setuptools-git',
            'tox',
        ],
    },
    entry_points={
        'fanstatic.libraries': [
            'deform = js.deform:library',
        ],
    },
)
