from setuptools import setup
setup(
    name='cli-anything-subfinder',
    version='1.0.0',
    packages=['cli_anything.subfinder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-subfinder=cli_anything.subfinder:cli']},
)
