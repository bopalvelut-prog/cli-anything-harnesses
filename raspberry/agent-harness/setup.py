from setuptools import setup
setup(
    name='cli-anything-raspberry',
    version='1.0.0',
    packages=['cli_anything.raspberry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-raspberry=cli_anything.raspberry:cli']},
)
