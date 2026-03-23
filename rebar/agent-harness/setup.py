from setuptools import setup
setup(
    name='cli-anything-rebar',
    version='1.0.0',
    packages=['cli_anything.rebar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rebar=cli_anything.rebar:cli']},
)
