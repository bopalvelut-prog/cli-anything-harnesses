from setuptools import setup
setup(
    name='cli-anything-erlang',
    version='1.0.0',
    packages=['cli_anything.erlang'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-erlang=cli_anything.erlang:cli']},
)
