from setuptools import setup
setup(
    name='cli-anything-log4j',
    version='1.0.0',
    packages=['cli_anything.log4j'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-log4j=cli_anything.log4j:cli']},
)
