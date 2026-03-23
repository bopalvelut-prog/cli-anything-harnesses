from setuptools import setup
setup(
    name='cli-anything-fast',
    version='1.0.0',
    packages=['cli_anything.fast'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fast=cli_anything.fast:cli']},
)
