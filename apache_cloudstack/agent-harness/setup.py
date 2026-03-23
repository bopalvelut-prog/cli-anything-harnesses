from setuptools import setup
setup(
    name='cli-anything-apache_cloudstack',
    version='1.0.0',
    packages=['cli_anything.apache_cloudstack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_cloudstack=cli_anything.apache_cloudstack:cli']},
)
