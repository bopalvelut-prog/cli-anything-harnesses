from setuptools import setup
setup(
    name='cli-anything-couchdb',
    version='1.0.0',
    packages=['cli_anything.couchdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-couchdb=cli_anything.couchdb:cli']},
)
