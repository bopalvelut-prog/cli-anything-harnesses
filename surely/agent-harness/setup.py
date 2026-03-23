from setuptools import setup
setup(
    name='cli-anything-surely',
    version='1.0.0',
    packages=['cli_anything.surely'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-surely=cli_anything.surely:cli']},
)
