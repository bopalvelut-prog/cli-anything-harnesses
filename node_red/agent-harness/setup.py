from setuptools import setup
setup(
    name='cli-anything-node_red',
    version='1.0.0',
    packages=['cli_anything.node_red'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-node_red=cli_anything.node_red:cli']},
)
