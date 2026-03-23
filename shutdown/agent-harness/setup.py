from setuptools import setup
setup(
    name='cli-anything-shutdown',
    version='1.0.0',
    packages=['cli_anything.shutdown'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shutdown=cli_anything.shutdown:cli']},
)
