from setuptools import setup
setup(
    name='cli-anything-though',
    version='1.0.0',
    packages=['cli_anything.though'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-though=cli_anything.though:cli']},
)
