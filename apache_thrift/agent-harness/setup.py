from setuptools import setup
setup(
    name='cli-anything-apache_thrift',
    version='1.0.0',
    packages=['cli_anything.apache_thrift'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_thrift=cli_anything.apache_thrift:cli']},
)
