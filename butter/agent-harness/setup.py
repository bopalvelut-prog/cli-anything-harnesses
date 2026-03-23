from setuptools import setup
setup(
    name='cli-anything-butter',
    version='1.0.0',
    packages=['cli_anything.butter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-butter=cli_anything.butter:cli']},
)
