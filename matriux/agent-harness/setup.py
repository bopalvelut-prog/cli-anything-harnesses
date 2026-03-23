from setuptools import setup
setup(
    name='cli-anything-matriux',
    version='1.0.0',
    packages=['cli_anything.matriux'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-matriux=cli_anything.matriux:cli']},
)
