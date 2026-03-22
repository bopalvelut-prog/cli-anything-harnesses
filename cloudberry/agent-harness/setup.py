from setuptools import setup
setup(
    name='cli-anything-cloudberry',
    version='1.0.0',
    packages=['cli_anything.cloudberry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudberry=cli_anything.cloudberry:cli']},
)
