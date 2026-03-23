from setuptools import setup
setup(
    name='cli-anything-purple',
    version='1.0.0',
    packages=['cli_anything.purple'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-purple=cli_anything.purple:cli']},
)
