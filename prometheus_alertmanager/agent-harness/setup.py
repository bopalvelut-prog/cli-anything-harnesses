from setuptools import setup
setup(
    name='cli-anything-prometheus_alertmanager',
    version='1.0.0',
    packages=['cli_anything.prometheus_alertmanager'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prometheus_alertmanager=cli_anything.prometheus_alertmanager:cli']},
)
