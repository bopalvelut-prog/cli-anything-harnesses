from setuptools import setup
setup(
    name='cli-anything-kafka',
    version='1.0.0',
    packages=['cli_anything.kafka'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kafka=cli_anything.kafka:cli']},
)
