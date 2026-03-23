from setuptools import setup
setup(
    name='cli-anything-metronome',
    version='1.0.0',
    packages=['cli_anything.metronome'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-metronome=cli_anything.metronome:cli']},
)
