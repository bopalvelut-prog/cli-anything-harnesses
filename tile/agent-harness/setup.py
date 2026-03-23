from setuptools import setup
setup(
    name='cli-anything-tile',
    version='1.0.0',
    packages=['cli_anything.tile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tile=cli_anything.tile:cli']},
)
