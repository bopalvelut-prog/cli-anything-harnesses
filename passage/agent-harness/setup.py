from setuptools import setup
setup(
    name='cli-anything-passage',
    version='1.0.0',
    packages=['cli_anything.passage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-passage=cli_anything.passage:cli']},
)
