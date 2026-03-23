from setuptools import setup
setup(
    name='cli-anything-apache_curator',
    version='1.0.0',
    packages=['cli_anything.apache_curator'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_curator=cli_anything.apache_curator:cli']},
)
