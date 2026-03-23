from setuptools import setup
setup(
    name='cli-anything-personal',
    version='1.0.0',
    packages=['cli_anything.personal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-personal=cli_anything.personal:cli']},
)
