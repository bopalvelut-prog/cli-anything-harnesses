from setuptools import setup
setup(
    name='cli-anything-helpscout',
    version='1.0.0',
    packages=['cli_anything.helpscout'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-helpscout=cli_anything.helpscout:cli']},
)
