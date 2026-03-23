from setuptools import setup
setup(
    name='cli-anything-pilot',
    version='1.0.0',
    packages=['cli_anything.pilot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pilot=cli_anything.pilot:cli']},
)
