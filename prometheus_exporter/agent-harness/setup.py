from setuptools import setup
setup(
    name='cli-anything-prometheus_exporter',
    version='1.0.0',
    packages=['cli_anything.prometheus_exporter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prometheus_exporter=cli_anything.prometheus_exporter:cli']},
)
