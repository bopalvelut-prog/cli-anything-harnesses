from setuptools import setup
setup(
    name='cli-anything-paxos',
    version='1.0.0',
    packages=['cli_anything.paxos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-paxos=cli_anything.paxos:cli']},
)
