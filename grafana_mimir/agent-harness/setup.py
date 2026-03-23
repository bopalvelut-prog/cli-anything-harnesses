from setuptools import setup
setup(
    name='cli-anything-grafana_mimir',
    version='1.0.0',
    packages=['cli_anything.grafana_mimir'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grafana_mimir=cli_anything.grafana_mimir:cli']},
)
