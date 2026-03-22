from setuptools import setup
setup(
    name='cli-anything-datadog',
    version='1.0.0',
    packages=['cli_anything.datadog'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-datadog=cli_anything.datadog:cli']},
)
