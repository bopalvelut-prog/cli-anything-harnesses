from setuptools import setup
setup(
    name='cli-anything-wedge',
    version='1.0.0',
    packages=['cli_anything.wedge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wedge=cli_anything.wedge:cli']},
)
