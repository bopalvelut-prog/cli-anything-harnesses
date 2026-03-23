from setuptools import setup
setup(
    name='cli-anything-year',
    version='1.0.0',
    packages=['cli_anything.year'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-year=cli_anything.year:cli']},
)
