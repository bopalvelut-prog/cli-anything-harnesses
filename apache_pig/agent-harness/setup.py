from setuptools import setup
setup(
    name='cli-anything-apache_pig',
    version='1.0.0',
    packages=['cli_anything.apache_pig'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_pig=cli_anything.apache_pig:cli']},
)
