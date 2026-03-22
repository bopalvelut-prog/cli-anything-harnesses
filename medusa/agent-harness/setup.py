from setuptools import setup
setup(
    name='cli-anything-medusa',
    version='1.0.0',
    packages=['cli_anything.medusa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-medusa=cli_anything.medusa:cli']},
)
