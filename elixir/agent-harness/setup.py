from setuptools import setup
setup(
    name='cli-anything-elixir',
    version='1.0.0',
    packages=['cli_anything.elixir'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-elixir=cli_anything.elixir:cli']},
)
