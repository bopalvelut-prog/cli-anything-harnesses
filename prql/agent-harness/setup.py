from setuptools import setup
setup(
    name='cli-anything-prql',
    version='1.0.0',
    packages=['cli_anything.prql'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prql=cli_anything.prql:cli']},
)
