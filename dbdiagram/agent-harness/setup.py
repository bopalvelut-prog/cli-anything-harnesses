from setuptools import setup
setup(
    name='cli-anything-dbdiagram',
    version='1.0.0',
    packages=['cli_anything.dbdiagram'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dbdiagram=cli_anything.dbdiagram:cli']},
)
