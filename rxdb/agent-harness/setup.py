from setuptools import setup
setup(
    name='cli-anything-rxdb',
    version='1.0.0',
    packages=['cli_anything.rxdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rxdb=cli_anything.rxdb:cli']},
)
