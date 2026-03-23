from setuptools import setup
setup(
    name='cli-anything-team',
    version='1.0.0',
    packages=['cli_anything.team'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-team=cli_anything.team:cli']},
)
