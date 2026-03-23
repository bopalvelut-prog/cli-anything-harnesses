from setuptools import setup
setup(
    name='cli-anything-coast',
    version='1.0.0',
    packages=['cli_anything.coast'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coast=cli_anything.coast:cli']},
)
