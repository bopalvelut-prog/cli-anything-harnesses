from setuptools import setup
setup(
    name='cli-anything-psycopg',
    version='1.0.0',
    packages=['cli_anything.psycopg'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-psycopg=cli_anything.psycopg:cli']},
)
