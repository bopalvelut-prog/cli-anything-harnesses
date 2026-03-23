from setuptools import setup
setup(
    name='cli-anything-flink',
    version='1.0.0',
    packages=['cli_anything.flink'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flink=cli_anything.flink:cli']},
)
