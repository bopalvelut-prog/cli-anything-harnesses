from setuptools import setup
setup(
    name='cli-anything-where',
    version='1.0.0',
    packages=['cli_anything.where'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-where=cli_anything.where:cli']},
)
