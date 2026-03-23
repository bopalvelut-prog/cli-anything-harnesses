from setuptools import setup
setup(
    name='cli-anything-avro_schema',
    version='1.0.0',
    packages=['cli_anything.avro_schema'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-avro_schema=cli_anything.avro_schema:cli']},
)
