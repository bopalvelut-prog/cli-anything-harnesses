from setuptools import setup
setup(
    name='cli-anything-unexpected',
    version='1.0.0',
    packages=['cli_anything.unexpected'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unexpected=cli_anything.unexpected:cli']},
)
