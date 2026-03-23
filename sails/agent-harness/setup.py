from setuptools import setup
setup(
    name='cli-anything-sails',
    version='1.0.0',
    packages=['cli_anything.sails'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sails=cli_anything.sails:cli']},
)
