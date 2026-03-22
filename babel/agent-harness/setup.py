from setuptools import setup
setup(
    name='cli-anything-babel',
    version='1.0.0',
    packages=['cli_anything.babel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-babel=cli_anything.babel:cli']},
)
