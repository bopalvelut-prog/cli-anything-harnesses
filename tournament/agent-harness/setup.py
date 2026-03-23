from setuptools import setup
setup(
    name='cli-anything-tournament',
    version='1.0.0',
    packages=['cli_anything.tournament'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tournament=cli_anything.tournament:cli']},
)
