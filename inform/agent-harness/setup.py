from setuptools import setup
setup(
    name='cli-anything-inform',
    version='1.0.0',
    packages=['cli_anything.inform'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-inform=cli_anything.inform:cli']},
)
