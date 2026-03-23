from setuptools import setup
setup(
    name='cli-anything-apache_maven',
    version='1.0.0',
    packages=['cli_anything.apache_maven'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_maven=cli_anything.apache_maven:cli']},
)
