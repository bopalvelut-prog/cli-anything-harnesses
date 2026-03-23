from setuptools import setup
setup(
    name='cli-anything-chart',
    version='1.0.0',
    packages=['cli_anything.chart'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chart=cli_anything.chart:cli']},
)
