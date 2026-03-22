from setuptools import setup
setup(
    name='cli-anything-dash',
    version='1.0.0',
    packages=['cli_anything.dash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dash=cli_anything.dash:cli']},
)
