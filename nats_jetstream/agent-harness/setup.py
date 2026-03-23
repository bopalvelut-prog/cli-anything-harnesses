from setuptools import setup
setup(
    name='cli-anything-nats_jetstream',
    version='1.0.0',
    packages=['cli_anything.nats_jetstream'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nats_jetstream=cli_anything.nats_jetstream:cli']},
)
