from setuptools import setup
setup(
    name='cli-anything-strike',
    version='1.0.0',
    packages=['cli_anything.strike'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-strike=cli_anything.strike:cli']},
)
