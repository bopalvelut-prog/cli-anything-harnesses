from setuptools import setup
setup(
    name='cli-anything-speaker',
    version='1.0.0',
    packages=['cli_anything.speaker'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-speaker=cli_anything.speaker:cli']},
)
