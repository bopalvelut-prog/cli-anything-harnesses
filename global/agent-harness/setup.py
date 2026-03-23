from setuptools import setup
setup(
    name='cli-anything-global',
    version='1.0.0',
    packages=['cli_anything.global'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-global=cli_anything.global:cli']},
)
