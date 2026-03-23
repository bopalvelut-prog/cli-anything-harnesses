from setuptools import setup
setup(
    name='cli-anything-orangepi',
    version='1.0.0',
    packages=['cli_anything.orangepi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-orangepi=cli_anything.orangepi:cli']},
)
