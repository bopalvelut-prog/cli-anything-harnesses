from setuptools import setup
setup(
    name='cli-anything-promote',
    version='1.0.0',
    packages=['cli_anything.promote'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-promote=cli_anything.promote:cli']},
)
