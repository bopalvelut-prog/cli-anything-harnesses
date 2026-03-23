from setuptools import setup
setup(
    name='cli-anything-db2',
    version='1.0.0',
    packages=['cli_anything.db2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-db2=cli_anything.db2:cli']},
)
