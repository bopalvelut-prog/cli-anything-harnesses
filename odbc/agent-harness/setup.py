from setuptools import setup
setup(
    name='cli-anything-odbc',
    version='1.0.0',
    packages=['cli_anything.odbc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-odbc=cli_anything.odbc:cli']},
)
