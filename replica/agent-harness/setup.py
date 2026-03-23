from setuptools import setup
setup(
    name='cli-anything-replica',
    version='1.0.0',
    packages=['cli_anything.replica'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-replica=cli_anything.replica:cli']},
)
