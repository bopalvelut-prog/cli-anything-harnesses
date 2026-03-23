from setuptools import setup
setup(
    name='cli-anything-aerospike',
    version='1.0.0',
    packages=['cli_anything.aerospike'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aerospike=cli_anything.aerospike:cli']},
)
