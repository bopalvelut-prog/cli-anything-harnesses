from setuptools import setup
setup(
    name='cli-anything-grafana_tempo',
    version='1.0.0',
    packages=['cli_anything.grafana_tempo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grafana_tempo=cli_anything.grafana_tempo:cli']},
)
