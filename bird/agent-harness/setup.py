from setuptools import setup
setup(
    name='cli-anything-bird',
    version='1.0.0',
    packages=['cli_anything.bird'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bird=cli_anything.bird:cli']},
)
