from setuptools import setup
setup(
    name='cli-anything-meal',
    version='1.0.0',
    packages=['cli_anything.meal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-meal=cli_anything.meal:cli']},
)
