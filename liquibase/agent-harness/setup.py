from setuptools import setup
setup(
    name='cli-anything-liquibase',
    version='1.0.0',
    packages=['cli_anything.liquibase'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-liquibase=cli_anything.liquibase:cli']},
)
