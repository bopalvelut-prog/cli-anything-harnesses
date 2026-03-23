from setuptools import setup
setup(
    name='cli-anything-organize',
    version='1.0.0',
    packages=['cli_anything.organize'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-organize=cli_anything.organize:cli']},
)
