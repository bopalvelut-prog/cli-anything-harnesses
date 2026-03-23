from setuptools import setup
setup(
    name='cli-anything-official',
    version='1.0.0',
    packages=['cli_anything.official'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-official=cli_anything.official:cli']},
)
