from setuptools import setup
setup(
    name='cli-anything-avro',
    version='1.0.0',
    packages=['cli_anything.avro'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-avro=cli_anything.avro:cli']},
)
