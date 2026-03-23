from setuptools import setup
setup(
    name='cli-anything-storm',
    version='1.0.0',
    packages=['cli_anything.storm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-storm=cli_anything.storm:cli']},
)
