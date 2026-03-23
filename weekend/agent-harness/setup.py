from setuptools import setup
setup(
    name='cli-anything-weekend',
    version='1.0.0',
    packages=['cli_anything.weekend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-weekend=cli_anything.weekend:cli']},
)
