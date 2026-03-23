from setuptools import setup
setup(
    name='cli-anything-ros',
    version='1.0.0',
    packages=['cli_anything.ros'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ros=cli_anything.ros:cli']},
)
