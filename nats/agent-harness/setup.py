from setuptools import setup
setup(
    name='cli-anything-nats',
    version='1.0.0',
    packages=['cli_anything.nats'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nats=cli_anything.nats:cli']},
)
