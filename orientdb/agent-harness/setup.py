from setuptools import setup
setup(
    name='cli-anything-orientdb',
    version='1.0.0',
    packages=['cli_anything.orientdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-orientdb=cli_anything.orientdb:cli']},
)
