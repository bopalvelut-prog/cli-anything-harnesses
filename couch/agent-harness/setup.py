from setuptools import setup
setup(
    name='cli-anything-couch',
    version='1.0.0',
    packages=['cli_anything.couch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-couch=cli_anything.couch:cli']},
)
