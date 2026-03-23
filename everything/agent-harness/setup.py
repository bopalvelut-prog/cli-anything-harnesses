from setuptools import setup
setup(
    name='cli-anything-everything',
    version='1.0.0',
    packages=['cli_anything.everything'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-everything=cli_anything.everything:cli']},
)
