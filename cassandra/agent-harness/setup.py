from setuptools import setup
setup(
    name='cli-anything-cassandra',
    version='1.0.0',
    packages=['cli_anything.cassandra'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cassandra=cli_anything.cassandra:cli']},
)
