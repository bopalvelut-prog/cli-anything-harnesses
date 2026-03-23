from setuptools import setup
setup(
    name='cli-anything-undertow',
    version='1.0.0',
    packages=['cli_anything.undertow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-undertow=cli_anything.undertow:cli']},
)
