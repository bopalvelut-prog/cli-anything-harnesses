from setuptools import setup
setup(
    name='cli-anything-super',
    version='1.0.0',
    packages=['cli_anything.super'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-super=cli_anything.super:cli']},
)
