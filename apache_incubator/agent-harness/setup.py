from setuptools import setup
setup(
    name='cli-anything-apache_incubator',
    version='1.0.0',
    packages=['cli_anything.apache_incubator'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_incubator=cli_anything.apache_incubator:cli']},
)
