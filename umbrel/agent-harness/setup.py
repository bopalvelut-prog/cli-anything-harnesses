from setuptools import setup
setup(
    name='cli-anything-umbrel',
    version='1.0.0',
    packages=['cli_anything.umbrel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-umbrel=cli_anything.umbrel:cli']},
)
