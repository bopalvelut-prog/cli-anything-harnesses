from setuptools import setup
setup(
    name='cli-anything-youngster',
    version='1.0.0',
    packages=['cli_anything.youngster'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-youngster=cli_anything.youngster:cli']},
)
