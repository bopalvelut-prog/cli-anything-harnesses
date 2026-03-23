from setuptools import setup
setup(
    name='cli-anything-ocean',
    version='1.0.0',
    packages=['cli_anything.ocean'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ocean=cli_anything.ocean:cli']},
)
