from setuptools import setup
setup(
    name='cli-anything-apache_couchdb',
    version='1.0.0',
    packages=['cli_anything.apache_couchdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_couchdb=cli_anything.apache_couchdb:cli']},
)
