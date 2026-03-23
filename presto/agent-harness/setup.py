from setuptools import setup
setup(
    name='cli-anything-presto',
    version='1.0.0',
    packages=['cli_anything.presto'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-presto=cli_anything.presto:cli']},
)
