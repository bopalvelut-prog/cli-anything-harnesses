from setuptools import setup
setup(
    name='cli-anything-gossip',
    version='1.0.0',
    packages=['cli_anything.gossip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gossip=cli_anything.gossip:cli']},
)
