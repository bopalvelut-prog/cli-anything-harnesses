from setuptools import setup
setup(
    name='cli-anything-figure',
    version='1.0.0',
    packages=['cli_anything.figure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-figure=cli_anything.figure:cli']},
)
