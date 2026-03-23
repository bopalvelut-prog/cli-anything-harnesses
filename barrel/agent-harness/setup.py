from setuptools import setup
setup(
    name='cli-anything-barrel',
    version='1.0.0',
    packages=['cli_anything.barrel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-barrel=cli_anything.barrel:cli']},
)
