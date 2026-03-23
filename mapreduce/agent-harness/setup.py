from setuptools import setup
setup(
    name='cli-anything-mapreduce',
    version='1.0.0',
    packages=['cli_anything.mapreduce'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mapreduce=cli_anything.mapreduce:cli']},
)
