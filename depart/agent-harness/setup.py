from setuptools import setup
setup(
    name='cli-anything-depart',
    version='1.0.0',
    packages=['cli_anything.depart'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-depart=cli_anything.depart:cli']},
)
