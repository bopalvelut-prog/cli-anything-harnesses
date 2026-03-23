from setuptools import setup
setup(
    name='cli-anything-grow',
    version='1.0.0',
    packages=['cli_anything.grow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grow=cli_anything.grow:cli']},
)
