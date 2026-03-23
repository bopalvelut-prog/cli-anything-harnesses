from setuptools import setup
setup(
    name='cli-anything-metrics_server',
    version='1.0.0',
    packages=['cli_anything.metrics_server'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-metrics_server=cli_anything.metrics_server:cli']},
)
