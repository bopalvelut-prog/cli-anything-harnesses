from setuptools import setup
setup(
    name='cli-anything-roxie',
    version='1.0.0',
    packages=['cli_anything.roxie'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-roxie=cli_anything.roxie:cli']},
)
