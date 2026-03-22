from setuptools import setup
setup(
    name='cli-anything-hashgraph',
    version='1.0.0',
    packages=['cli_anything.hashgraph'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hashgraph=cli_anything.hashgraph:cli']},
)
