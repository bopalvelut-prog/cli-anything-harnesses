from setuptools import setup
setup(
    name='cli-anything-molecule',
    version='1.0.0',
    packages=['cli_anything.molecule'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-molecule=cli_anything.molecule:cli']},
)
