from setuptools import setup
setup(
    name='cli-anything-autom',
    version='1.0.0',
    packages=['cli_anything.autom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autom=cli_anything.autom:cli']},
)
