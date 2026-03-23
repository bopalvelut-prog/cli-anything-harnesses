from setuptools import setup
setup(
    name='cli-anything-unit',
    version='1.0.0',
    packages=['cli_anything.unit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unit=cli_anything.unit:cli']},
)
