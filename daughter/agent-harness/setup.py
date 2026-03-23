from setuptools import setup
setup(
    name='cli-anything-daughter',
    version='1.0.0',
    packages=['cli_anything.daughter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-daughter=cli_anything.daughter:cli']},
)
