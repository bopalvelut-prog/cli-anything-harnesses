from setuptools import setup
setup(
    name='cli-anything-bite',
    version='1.0.0',
    packages=['cli_anything.bite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bite=cli_anything.bite:cli']},
)
