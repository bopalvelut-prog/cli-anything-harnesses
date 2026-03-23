from setuptools import setup
setup(
    name='cli-anything-apache_log4j',
    version='1.0.0',
    packages=['cli_anything.apache_log4j'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_log4j=cli_anything.apache_log4j:cli']},
)
