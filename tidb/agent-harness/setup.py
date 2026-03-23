from setuptools import setup
setup(
    name='cli-anything-tidb',
    version='1.0.0',
    packages=['cli_anything.tidb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tidb=cli_anything.tidb:cli']},
)
