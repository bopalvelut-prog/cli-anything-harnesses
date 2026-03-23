from setuptools import setup
setup(
    name='cli-anything-kafka_streams',
    version='1.0.0',
    packages=['cli_anything.kafka_streams'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kafka_streams=cli_anything.kafka_streams:cli']},
)
