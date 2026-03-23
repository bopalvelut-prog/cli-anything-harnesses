from setuptools import setup
setup(
    name='cli-anything-archive',
    version='1.0.0',
    packages=['cli_anything.archive'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-archive=cli_anything.archive:cli']},
)
