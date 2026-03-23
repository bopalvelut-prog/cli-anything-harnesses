from setuptools import setup
setup(
    name='cli-anything-apache_karaf',
    version='1.0.0',
    packages=['cli_anything.apache_karaf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_karaf=cli_anything.apache_karaf:cli']},
)
