from setuptools import setup
setup(
    name='cli-anything-node',
    version='1.0.0',
    packages=['cli_anything.node'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-node=cli_anything.node:cli']},
)
