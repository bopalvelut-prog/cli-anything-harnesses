from setuptools import setup
setup(
    name='cli-anything-mazerunner',
    version='1.0.0',
    packages=['cli_anything.mazerunner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mazerunner=cli_anything.mazerunner:cli']},
)
