from setuptools import setup
setup(
    name='cli-anything-protobuf',
    version='1.0.0',
    packages=['cli_anything.protobuf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-protobuf=cli_anything.protobuf:cli']},
)
