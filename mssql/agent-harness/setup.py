from setuptools import setup
setup(
    name='cli-anything-mssql',
    version='1.0.0',
    packages=['cli_anything.mssql'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mssql=cli_anything.mssql:cli']},
)
