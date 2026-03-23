from setuptools import setup
setup(
    name='cli-anything-prometheus_push',
    version='1.0.0',
    packages=['cli_anything.prometheus_push'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prometheus_push=cli_anything.prometheus_push:cli']},
)
