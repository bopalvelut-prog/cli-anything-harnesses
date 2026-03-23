from setuptools import setup
setup(
    name='cli-anything-scripting',
    version='1.0.0',
    packages=['cli_anything.scripting'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scripting=cli_anything.scripting:cli']},
)
