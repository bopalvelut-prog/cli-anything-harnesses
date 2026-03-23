from setuptools import setup
setup(
    name='cli-anything-calm',
    version='1.0.0',
    packages=['cli_anything.calm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-calm=cli_anything.calm:cli']},
)
