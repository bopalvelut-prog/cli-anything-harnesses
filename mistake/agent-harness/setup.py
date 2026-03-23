from setuptools import setup
setup(
    name='cli-anything-mistake',
    version='1.0.0',
    packages=['cli_anything.mistake'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mistake=cli_anything.mistake:cli']},
)
