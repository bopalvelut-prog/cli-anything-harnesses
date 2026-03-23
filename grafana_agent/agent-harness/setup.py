from setuptools import setup
setup(
    name='cli-anything-grafana_agent',
    version='1.0.0',
    packages=['cli_anything.grafana_agent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grafana_agent=cli_anything.grafana_agent:cli']},
)
