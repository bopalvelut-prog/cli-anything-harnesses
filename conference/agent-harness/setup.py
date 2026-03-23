from setuptools import setup
setup(
    name='cli-anything-conference',
    version='1.0.0',
    packages=['cli_anything.conference'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-conference=cli_anything.conference:cli']},
)
