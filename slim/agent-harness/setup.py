from setuptools import setup
setup(
    name='cli-anything-slim',
    version='1.0.0',
    packages=['cli_anything.slim'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slim=cli_anything.slim:cli']},
)
