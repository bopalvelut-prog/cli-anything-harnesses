from setuptools import setup
setup(
    name='cli-anything-gorilla',
    version='1.0.0',
    packages=['cli_anything.gorilla'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gorilla=cli_anything.gorilla:cli']},
)
