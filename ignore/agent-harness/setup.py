from setuptools import setup
setup(
    name='cli-anything-ignore',
    version='1.0.0',
    packages=['cli_anything.ignore'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ignore=cli_anything.ignore:cli']},
)
