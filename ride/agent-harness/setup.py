from setuptools import setup
setup(
    name='cli-anything-ride',
    version='1.0.0',
    packages=['cli_anything.ride'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ride=cli_anything.ride:cli']},
)
