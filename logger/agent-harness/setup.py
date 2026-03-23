from setuptools import setup
setup(
    name='cli-anything-logger',
    version='1.0.0',
    packages=['cli_anything.logger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-logger=cli_anything.logger:cli']},
)
