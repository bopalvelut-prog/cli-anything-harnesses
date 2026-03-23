from setuptools import setup
setup(
    name='cli-anything-estate',
    version='1.0.0',
    packages=['cli_anything.estate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-estate=cli_anything.estate:cli']},
)
