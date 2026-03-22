from setuptools import setup
setup(
    name='cli-anything-ubiquiti',
    version='1.0.0',
    packages=['cli_anything.ubiquiti'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ubiquiti=cli_anything.ubiquiti:cli']},
)
