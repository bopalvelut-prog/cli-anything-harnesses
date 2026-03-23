from setuptools import setup
setup(
    name='cli-anything-well',
    version='1.0.0',
    packages=['cli_anything.well'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-well=cli_anything.well:cli']},
)
