from setuptools import setup
setup(
    name='cli-anything-proto',
    version='1.0.0',
    packages=['cli_anything.proto'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-proto=cli_anything.proto:cli']},
)
