from setuptools import setup
setup(
    name='cli-anything-partly',
    version='1.0.0',
    packages=['cli_anything.partly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-partly=cli_anything.partly:cli']},
)
