from setuptools import setup
setup(
    name='cli-anything-robot',
    version='1.0.0',
    packages=['cli_anything.robot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-robot=cli_anything.robot:cli']},
)
