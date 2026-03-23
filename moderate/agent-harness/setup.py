from setuptools import setup
setup(
    name='cli-anything-moderate',
    version='1.0.0',
    packages=['cli_anything.moderate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-moderate=cli_anything.moderate:cli']},
)
