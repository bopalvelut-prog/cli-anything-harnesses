from setuptools import setup
setup(
    name='cli-anything-cucumber',
    version='1.0.0',
    packages=['cli_anything.cucumber'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cucumber=cli_anything.cucumber:cli']},
)
