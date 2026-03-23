from setuptools import setup
setup(
    name='cli-anything-raspbian',
    version='1.0.0',
    packages=['cli_anything.raspbian'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-raspbian=cli_anything.raspbian:cli']},
)
