from setuptools import setup
setup(
    name='cli-anything-dirk',
    version='1.0.0',
    packages=['cli_anything.dirk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dirk=cli_anything.dirk:cli']},
)
