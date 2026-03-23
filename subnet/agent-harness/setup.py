from setuptools import setup
setup(
    name='cli-anything-subnet',
    version='1.0.0',
    packages=['cli_anything.subnet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-subnet=cli_anything.subnet:cli']},
)
