from setuptools import setup
setup(
    name='cli-anything-raft',
    version='1.0.0',
    packages=['cli_anything.raft'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-raft=cli_anything.raft:cli']},
)
