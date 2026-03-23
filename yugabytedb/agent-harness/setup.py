from setuptools import setup
setup(
    name='cli-anything-yugabytedb',
    version='1.0.0',
    packages=['cli_anything.yugabytedb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yugabytedb=cli_anything.yugabytedb:cli']},
)
