from setuptools import setup
setup(
    name='cli-anything-keystone',
    version='1.0.0',
    packages=['cli_anything.keystone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-keystone=cli_anything.keystone:cli']},
)
