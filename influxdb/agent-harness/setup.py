from setuptools import setup
setup(
    name='cli-anything-influxdb',
    version='1.0.0',
    packages=['cli_anything.influxdb'],
    install_requires=['click', 'influxdb-client'],
    entry_points={'console_scripts': ['cli-anything-influxdb=cli_anything.influxdb:cli']},
)
