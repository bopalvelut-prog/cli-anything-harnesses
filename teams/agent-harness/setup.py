from setuptools import setup
setup(
    name='cli-anything-teams',
    version='1.0.0',
    packages=['cli_anything.teams'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-teams=cli_anything.teams:cli']},
)
