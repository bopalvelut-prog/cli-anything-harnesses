from setuptools import setup
setup(
    name='cli-anything-nats_streaming',
    version='1.0.0',
    packages=['cli_anything.nats_streaming'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nats_streaming=cli_anything.nats_streaming:cli']},
)
