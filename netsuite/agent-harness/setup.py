from setuptools import setup
setup(
    name='cli-anything-netsuite',
    version='1.0.0',
    packages=['cli_anything.netsuite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-netsuite=cli_anything.netsuite:cli']},
)
