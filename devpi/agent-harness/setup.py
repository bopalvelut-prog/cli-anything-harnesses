from setuptools import setup
setup(
    name='cli-anything-devpi',
    version='1.0.0',
    packages=['cli_anything.devpi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-devpi=cli_anything.devpi:cli']},
)
