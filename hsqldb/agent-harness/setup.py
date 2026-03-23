from setuptools import setup
setup(
    name='cli-anything-hsqldb',
    version='1.0.0',
    packages=['cli_anything.hsqldb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hsqldb=cli_anything.hsqldb:cli']},
)
