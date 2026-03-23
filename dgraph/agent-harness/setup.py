from setuptools import setup
setup(
    name='cli-anything-dgraph',
    version='1.0.0',
    packages=['cli_anything.dgraph'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dgraph=cli_anything.dgraph:cli']},
)
