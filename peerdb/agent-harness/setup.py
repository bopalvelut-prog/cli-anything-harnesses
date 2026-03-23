from setuptools import setup
setup(
    name='cli-anything-peerdb',
    version='1.0.0',
    packages=['cli_anything.peerdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-peerdb=cli_anything.peerdb:cli']},
)
