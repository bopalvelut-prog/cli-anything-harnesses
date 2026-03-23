from setuptools import setup
setup(
    name='cli-anything-parse',
    version='1.0.0',
    packages=['cli_anything.parse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-parse=cli_anything.parse:cli']},
)
