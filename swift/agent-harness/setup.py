from setuptools import setup
setup(
    name='cli-anything-swift',
    version='1.0.0',
    packages=['cli_anything.swift'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-swift=cli_anything.swift:cli']},
)
