from setuptools import setup
setup(
    name='cli-anything-oracle_db',
    version='1.0.0',
    packages=['cli_anything.oracle_db'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-oracle_db=cli_anything.oracle_db:cli']},
)
