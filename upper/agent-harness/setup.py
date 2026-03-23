from setuptools import setup
setup(
    name='cli-anything-upper',
    version='1.0.0',
    packages=['cli_anything.upper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-upper=cli_anything.upper:cli']},
)
