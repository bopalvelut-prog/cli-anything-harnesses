from setuptools import setup
setup(
    name='cli-anything-guilt',
    version='1.0.0',
    packages=['cli_anything.guilt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-guilt=cli_anything.guilt:cli']},
)
