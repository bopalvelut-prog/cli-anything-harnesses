from setuptools import setup
setup(
    name='cli-anything-hbase',
    version='1.0.0',
    packages=['cli_anything.hbase'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hbase=cli_anything.hbase:cli']},
)
