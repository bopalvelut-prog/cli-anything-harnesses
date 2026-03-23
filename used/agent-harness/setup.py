from setuptools import setup
setup(
    name='cli-anything-used',
    version='1.0.0',
    packages=['cli_anything.used'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-used=cli_anything.used:cli']},
)
