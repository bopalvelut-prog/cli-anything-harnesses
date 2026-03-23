from setuptools import setup
setup(
    name='cli-anything-dispatch',
    version='1.0.0',
    packages=['cli_anything.dispatch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dispatch=cli_anything.dispatch:cli']},
)
