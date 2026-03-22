from setuptools import setup
setup(
    name='cli-anything-hasura',
    version='1.0.0',
    packages=['cli_anything.hasura'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hasura=cli_anything.hasura:cli']},
)
