from setuptools import setup
setup(
    name='cli-anything-ddwrt',
    version='1.0.0',
    packages=['cli_anything.ddwrt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ddwrt=cli_anything.ddwrt:cli']},
)
