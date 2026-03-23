from setuptools import setup
setup(
    name='cli-anything-oauth',
    version='1.0.0',
    packages=['cli_anything.oauth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-oauth=cli_anything.oauth:cli']},
)
