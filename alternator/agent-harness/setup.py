from setuptools import setup
setup(
    name='cli-anything-alternator',
    version='1.0.0',
    packages=['cli_anything.alternator'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alternator=cli_anything.alternator:cli']},
)
