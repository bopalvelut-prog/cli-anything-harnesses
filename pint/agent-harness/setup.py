from setuptools import setup
setup(
    name='cli-anything-pint',
    version='1.0.0',
    packages=['cli_anything.pint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pint=cli_anything.pint:cli']},
)
