from setuptools import setup
setup(
    name='cli-anything-economy',
    version='1.0.0',
    packages=['cli_anything.economy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-economy=cli_anything.economy:cli']},
)
