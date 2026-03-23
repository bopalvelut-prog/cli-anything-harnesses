from setuptools import setup
setup(
    name='cli-anything-include',
    version='1.0.0',
    packages=['cli_anything.include'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-include=cli_anything.include:cli']},
)
