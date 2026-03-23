from setuptools import setup
setup(
    name='cli-anything-highcharts',
    version='1.0.0',
    packages=['cli_anything.highcharts'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-highcharts=cli_anything.highcharts:cli']},
)
