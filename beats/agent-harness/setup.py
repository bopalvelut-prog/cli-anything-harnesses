from setuptools import setup
setup(
    name='cli-anything-beats',
    version='1.0.0',
    packages=['cli_anything.beats'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-beats=cli_anything.beats:cli']},
)
