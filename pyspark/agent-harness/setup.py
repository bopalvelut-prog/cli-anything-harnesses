from setuptools import setup
setup(
    name='cli-anything-pyspark',
    version='1.0.0',
    packages=['cli_anything.pyspark'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pyspark=cli_anything.pyspark:cli']},
)
