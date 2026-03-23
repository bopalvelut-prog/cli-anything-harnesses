from setuptools import setup
setup(
    name='cli-anything-particle',
    version='1.0.0',
    packages=['cli_anything.particle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-particle=cli_anything.particle:cli']},
)
