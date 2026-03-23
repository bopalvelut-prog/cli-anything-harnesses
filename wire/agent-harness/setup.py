from setuptools import setup
setup(
    name='cli-anything-wire',
    version='1.0.0',
    packages=['cli_anything.wire'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wire=cli_anything.wire:cli']},
)
