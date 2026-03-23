from setuptools import setup
setup(
    name='cli-anything-kafka_connect',
    version='1.0.0',
    packages=['cli_anything.kafka_connect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kafka_connect=cli_anything.kafka_connect:cli']},
)
