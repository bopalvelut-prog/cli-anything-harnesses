from setuptools import setup
setup(
    name='cli-anything-reactor',
    version='1.0.0',
    packages=['cli_anything.reactor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reactor=cli_anything.reactor:cli']},
)
