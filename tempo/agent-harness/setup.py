from setuptools import setup
setup(
    name='cli-anything-tempo',
    version='1.0.0',
    packages=['cli_anything.tempo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tempo=cli_anything.tempo:cli']},
)
