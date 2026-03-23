from setuptools import setup
setup(
    name='cli-anything-participate',
    version='1.0.0',
    packages=['cli_anything.participate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-participate=cli_anything.participate:cli']},
)
