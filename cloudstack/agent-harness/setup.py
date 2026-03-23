from setuptools import setup
setup(
    name='cli-anything-cloudstack',
    version='1.0.0',
    packages=['cli_anything.cloudstack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudstack=cli_anything.cloudstack:cli']},
)
