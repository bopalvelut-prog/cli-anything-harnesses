from setuptools import setup
setup(
    name='cli-anything-apache_sqoop',
    version='1.0.0',
    packages=['cli_anything.apache_sqoop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_sqoop=cli_anything.apache_sqoop:cli']},
)
