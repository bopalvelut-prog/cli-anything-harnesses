from setuptools import setup
setup(
    name='cli-anything-greenplum',
    version='1.0.0',
    packages=['cli_anything.greenplum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-greenplum=cli_anything.greenplum:cli']},
)
