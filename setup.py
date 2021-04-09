# coding: utf-8
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setupargs = {
    'name': 'mywatch',
    'description': 'Provides an ORM for MySQL, PostgreSQL and SQLite.',

    'license': 'GPLv3',
    'version': '0.0.1',

    'long_description': long_description,
    'long_description_content_type': 'text/markdown',

    'scripts': ['mywatch.py'],
    'author': 'Christian Kokoska',
    'author_email': 'info@softcreate.de',
    'install_requires': [
        'checksumdir'
    ],
}

if __name__ == '__main__':
    setup(**setupargs)
