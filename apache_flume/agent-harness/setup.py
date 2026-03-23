from setuptools import setup
setup(
    name='cli-anything-apache_flume',
    version='1.0.0',
    packages=['cli_anything.apache_flume'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_flume=cli_anything.apache_flume:cli']},
)
