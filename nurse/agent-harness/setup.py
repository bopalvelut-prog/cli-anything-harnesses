from setuptools import setup
setup(
    name='cli-anything-nurse',
    version='1.0.0',
    packages=['cli_anything.nurse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nurse=cli_anything.nurse:cli']},
)
