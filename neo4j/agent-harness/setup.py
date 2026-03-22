from setuptools import setup
setup(
    name='cli-anything-neo4j',
    version='1.0.0',
    packages=['cli_anything.neo4j'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-neo4j=cli_anything.neo4j:cli']},
)
