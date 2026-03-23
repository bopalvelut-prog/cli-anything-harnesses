from setuptools import setup
setup(
    name='cli-anything-rebar3',
    version='1.0.0',
    packages=['cli_anything.rebar3'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rebar3=cli_anything.rebar3:cli']},
)
