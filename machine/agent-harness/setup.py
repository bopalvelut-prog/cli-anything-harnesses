from setuptools import setup
setup(
    name='cli-anything-machine',
    version='1.0.0',
    packages=['cli_anything.machine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-machine=cli_anything.machine:cli']},
)
