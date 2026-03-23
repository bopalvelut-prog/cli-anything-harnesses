from setuptools import setup
setup(
    name='cli-anything-smart',
    version='1.0.0',
    packages=['cli_anything.smart'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-smart=cli_anything.smart:cli']},
)
