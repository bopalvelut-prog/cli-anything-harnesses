from setuptools import setup
setup(
    name='cli-anything-hdfs',
    version='1.0.0',
    packages=['cli_anything.hdfs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hdfs=cli_anything.hdfs:cli']},
)
