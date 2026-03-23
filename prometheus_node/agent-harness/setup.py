from setuptools import setup
setup(
    name='cli-anything-prometheus_node',
    version='1.0.0',
    packages=['cli_anything.prometheus_node'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prometheus_node=cli_anything.prometheus_node:cli']},
)
