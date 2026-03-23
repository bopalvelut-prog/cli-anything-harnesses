from setuptools import setup
setup(
    name='cli-anything-fault',
    version='1.0.0',
    packages=['cli_anything.fault'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fault=cli_anything.fault:cli']},
)
