from setuptools import setup
setup(
    name='cli-anything-applescript',
    version='1.0.0',
    packages=['cli_anything.applescript'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-applescript=cli_anything.applescript:cli']},
)
