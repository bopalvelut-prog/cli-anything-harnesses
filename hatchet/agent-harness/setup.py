from setuptools import setup
setup(
    name='cli-anything-hatchet',
    version='1.0.0',
    packages=['cli_anything.hatchet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hatchet=cli_anything.hatchet:cli']},
)
