from setuptools import setup
setup(
    name='cli-anything-bore',
    version='1.0.0',
    packages=['cli_anything.bore'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bore=cli_anything.bore:cli']},
)
