from setuptools import setup
setup(
    name='cli-anything-gollum',
    version='1.0.0',
    packages=['cli_anything.gollum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gollum=cli_anything.gollum:cli']},
)
