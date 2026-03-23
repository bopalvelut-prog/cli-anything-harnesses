from setuptools import setup
setup(
    name='cli-anything-sophisticated',
    version='1.0.0',
    packages=['cli_anything.sophisticated'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sophisticated=cli_anything.sophisticated:cli']},
)
