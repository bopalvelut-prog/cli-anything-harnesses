from setuptools import setup
setup(
    name='cli-anything-plumber',
    version='1.0.0',
    packages=['cli_anything.plumber'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plumber=cli_anything.plumber:cli']},
)
