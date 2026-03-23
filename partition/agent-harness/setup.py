from setuptools import setup
setup(
    name='cli-anything-partition',
    version='1.0.0',
    packages=['cli_anything.partition'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-partition=cli_anything.partition:cli']},
)
