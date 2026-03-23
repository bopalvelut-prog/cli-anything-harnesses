from setuptools import setup
setup(
    name='cli-anything-pyodbc',
    version='1.0.0',
    packages=['cli_anything.pyodbc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pyodbc=cli_anything.pyodbc:cli']},
)
