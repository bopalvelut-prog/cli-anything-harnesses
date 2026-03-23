from setuptools import setup
setup(
    name='cli-anything-clap',
    version='1.0.0',
    packages=['cli_anything.clap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clap=cli_anything.clap:cli']},
)
