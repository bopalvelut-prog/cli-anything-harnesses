from setuptools import setup
setup(
    name='cli-anything-checkmarx',
    version='1.0.0',
    packages=['cli_anything.checkmarx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-checkmarx=cli_anything.checkmarx:cli']},
)
