from setuptools import setup
setup(
    name='cli-anything-graphite',
    version='1.0.0',
    packages=['cli_anything.graphite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-graphite=cli_anything.graphite:cli']},
)
