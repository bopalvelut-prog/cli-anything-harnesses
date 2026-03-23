from setuptools import setup
setup(
    name='cli-anything-rethinkdb',
    version='1.0.0',
    packages=['cli_anything.rethinkdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rethinkdb=cli_anything.rethinkdb:cli']},
)
