from setuptools import setup
setup(
    name='cli-anything-mpich',
    version='1.0.0',
    packages=['cli_anything.mpich'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mpich=cli_anything.mpich:cli']},
)
