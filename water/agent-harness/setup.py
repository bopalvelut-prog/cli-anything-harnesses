from setuptools import setup
setup(
    name='cli-anything-water',
    version='1.0.0',
    packages=['cli_anything.water'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-water=cli_anything.water:cli']},
)
