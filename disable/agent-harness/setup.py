from setuptools import setup
setup(
    name='cli-anything-disable',
    version='1.0.0',
    packages=['cli_anything.disable'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-disable=cli_anything.disable:cli']},
)
