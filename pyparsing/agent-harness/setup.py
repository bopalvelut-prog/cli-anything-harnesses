from setuptools import setup
setup(
    name='cli-anything-pyparsing',
    version='1.0.0',
    packages=['cli_anything.pyparsing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pyparsing=cli_anything.pyparsing:cli']},
)
