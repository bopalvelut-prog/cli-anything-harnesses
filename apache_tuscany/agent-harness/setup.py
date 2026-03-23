from setuptools import setup
setup(
    name='cli-anything-apache_tuscany',
    version='1.0.0',
    packages=['cli_anything.apache_tuscany'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_tuscany=cli_anything.apache_tuscany:cli']},
)
