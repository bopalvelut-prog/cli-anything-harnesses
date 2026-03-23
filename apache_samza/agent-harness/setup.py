from setuptools import setup
setup(
    name='cli-anything-apache_samza',
    version='1.0.0',
    packages=['cli_anything.apache_samza'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_samza=cli_anything.apache_samza:cli']},
)
