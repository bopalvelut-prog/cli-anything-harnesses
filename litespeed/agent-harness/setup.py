from setuptools import setup
setup(
    name='cli-anything-litespeed',
    version='1.0.0',
    packages=['cli_anything.litespeed'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-litespeed=cli_anything.litespeed:cli']},
)
