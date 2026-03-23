from setuptools import setup
setup(
    name='cli-anything-creature',
    version='1.0.0',
    packages=['cli_anything.creature'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-creature=cli_anything.creature:cli']},
)
