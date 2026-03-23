from setuptools import setup
setup(
    name='cli-anything-plsql',
    version='1.0.0',
    packages=['cli_anything.plsql'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plsql=cli_anything.plsql:cli']},
)
