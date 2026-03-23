from setuptools import setup
setup(
    name='cli-anything-table',
    version='1.0.0',
    packages=['cli_anything.table'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-table=cli_anything.table:cli']},
)
