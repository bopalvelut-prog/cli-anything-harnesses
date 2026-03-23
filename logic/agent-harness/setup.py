from setuptools import setup
setup(
    name='cli-anything-logic',
    version='1.0.0',
    packages=['cli_anything.logic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-logic=cli_anything.logic:cli']},
)
