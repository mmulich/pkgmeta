# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

name = 'pkgmeta'
version = '0.1'

install_requires = [
    'setuptools',
    ]
test_requires = [
    ]
if sys.version_info < (2, 7,):
    test_requires.append('unittest2')
extras_require = {'test': test_requires}

long_description = '\n\n'.join([
        read('README.rst'),
        read('docs', 'source', 'changes.rst'),
])

entry_points = """\
[console_scripts]
pkgmeta = pkgmeta.cli:main
"""

DEV_STATES = [
    "Development Status :: 3 - Alpha",
    "Development Status :: 4 - Beta",
    "Development Status :: 5 - Production/Stable",
]
if version.find('a') >= 0:
    state = 0
elif version.find('b') >= 0:
    state = 1
else:
    state = 2
development_status = DEV_STATES[state]

setup(
    name=name,
    version=version,
    author="Michael Mulich",
    author_email="michael.mulich@gmail.com",
    description="Python distribution metadata repository",
    long_description=long_description,
    url="https://github.com/pumazi/pkgmeta",
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        development_status,
        ],
    keywords='',
    license='GPL',
    packages=find_packages(),
    install_requires=install_requires,
    extras_require=extras_require,
    include_package_data=True,
    zip_safe=False,
    entry_points=entry_points,
    )
