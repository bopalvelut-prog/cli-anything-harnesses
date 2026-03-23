from setuptools import setup
setup(
    name='cli-anything-either',
    version='1.0.0',
    packages=['cli_anything.either'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-either=cli_anything.either:cli']},
)
