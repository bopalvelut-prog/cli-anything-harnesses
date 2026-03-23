from setuptools import setup
setup(
    name='cli-anything-decorate',
    version='1.0.0',
    packages=['cli_anything.decorate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-decorate=cli_anything.decorate:cli']},
)
