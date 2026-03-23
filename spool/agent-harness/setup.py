from setuptools import setup
setup(
    name='cli-anything-spool',
    version='1.0.0',
    packages=['cli_anything.spool'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spool=cli_anything.spool:cli']},
)
