from setuptools import setup
setup(
    name='cli-anything-grafana_loki',
    version='1.0.0',
    packages=['cli_anything.grafana_loki'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grafana_loki=cli_anything.grafana_loki:cli']},
)
