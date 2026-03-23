from setuptools import setup
setup(
    name='cli-anything-graph',
    version='1.0.0',
    packages=['cli_anything.graph'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-graph=cli_anything.graph:cli']},
)
