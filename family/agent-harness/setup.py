from setuptools import setup
setup(
    name='cli-anything-family',
    version='1.0.0',
    packages=['cli_anything.family'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-family=cli_anything.family:cli']},
)
