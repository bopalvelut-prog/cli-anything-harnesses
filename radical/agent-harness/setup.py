from setuptools import setup
setup(
    name='cli-anything-radical',
    version='1.0.0',
    packages=['cli_anything.radical'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-radical=cli_anything.radical:cli']},
)
