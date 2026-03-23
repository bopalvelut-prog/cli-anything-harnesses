from setuptools import setup
setup(
    name='cli-anything-yesterday',
    version='1.0.0',
    packages=['cli_anything.yesterday'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yesterday=cli_anything.yesterday:cli']},
)
