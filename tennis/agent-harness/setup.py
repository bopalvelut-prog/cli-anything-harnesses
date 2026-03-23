from setuptools import setup
setup(
    name='cli-anything-tennis',
    version='1.0.0',
    packages=['cli_anything.tennis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tennis=cli_anything.tennis:cli']},
)
