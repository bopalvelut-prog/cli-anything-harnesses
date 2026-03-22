from setuptools import setup
setup(
    name='cli-anything-craft',
    version='1.0.0',
    packages=['cli_anything.craft'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-craft=cli_anything.craft:cli']},
)
