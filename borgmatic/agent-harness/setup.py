from setuptools import setup
setup(
    name='cli-anything-borgmatic',
    version='1.0.0',
    packages=['cli_anything.borgmatic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-borgmatic=cli_anything.borgmatic:cli']},
)
