from setuptools import setup
setup(
    name='cli-anything-pegasus',
    version='1.0.0',
    packages=['cli_anything.pegasus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pegasus=cli_anything.pegasus:cli']},
)
