from setuptools import setup
setup(
    name='cli-anything-debian',
    version='1.0.0',
    packages=['cli_anything.debian'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-debian=cli_anything.debian:cli']},
)
