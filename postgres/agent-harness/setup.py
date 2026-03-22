from setuptools import setup
setup(
    name='cli-anything-postgres',
    version='1.0.0',
    packages=['cli_anything.postgres'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-postgres=cli_anything.postgres:cli']},
)
