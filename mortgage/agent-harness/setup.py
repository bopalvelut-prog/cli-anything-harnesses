from setuptools import setup
setup(
    name='cli-anything-mortgage',
    version='1.0.0',
    packages=['cli_anything.mortgage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mortgage=cli_anything.mortgage:cli']},
)
