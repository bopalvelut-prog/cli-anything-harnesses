from setuptools import setup
setup(
    name='cli-anything-sheet',
    version='1.0.0',
    packages=['cli_anything.sheet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sheet=cli_anything.sheet:cli']},
)
