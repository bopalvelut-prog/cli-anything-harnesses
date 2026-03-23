from setuptools import setup
setup(
    name='cli-anything-architecture',
    version='1.0.0',
    packages=['cli_anything.architecture'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-architecture=cli_anything.architecture:cli']},
)
