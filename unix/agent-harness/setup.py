from setuptools import setup
setup(
    name='cli-anything-unix',
    version='1.0.0',
    packages=['cli_anything.unix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unix=cli_anything.unix:cli']},
)
