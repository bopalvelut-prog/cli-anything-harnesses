from setuptools import setup
setup(
    name='cli-anything-brass',
    version='1.0.0',
    packages=['cli_anything.brass'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brass=cli_anything.brass:cli']},
)
