from setuptools import setup
setup(
    name='cli-anything-help',
    version='1.0.0',
    packages=['cli_anything.help'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-help=cli_anything.help:cli']},
)
