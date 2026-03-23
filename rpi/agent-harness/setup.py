from setuptools import setup
setup(
    name='cli-anything-rpi',
    version='1.0.0',
    packages=['cli_anything.rpi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rpi=cli_anything.rpi:cli']},
)
