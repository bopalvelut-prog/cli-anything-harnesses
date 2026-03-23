from setuptools import setup
setup(
    name='cli-anything-chance',
    version='1.0.0',
    packages=['cli_anything.chance'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chance=cli_anything.chance:cli']},
)
