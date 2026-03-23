from setuptools import setup
setup(
    name='cli-anything-duckdb',
    version='1.0.0',
    packages=['cli_anything.duckdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-duckdb=cli_anything.duckdb:cli']},
)
