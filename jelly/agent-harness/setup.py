from setuptools import setup
setup(
    name='cli-anything-jelly',
    version='1.0.0',
    packages=['cli_anything.jelly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jelly=cli_anything.jelly:cli']},
)
