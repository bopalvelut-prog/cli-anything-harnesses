from setuptools import setup
setup(
    name='cli-anything-blond',
    version='1.0.0',
    packages=['cli_anything.blond'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-blond=cli_anything.blond:cli']},
)
