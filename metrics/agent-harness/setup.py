from setuptools import setup
setup(
    name='cli-anything-metrics',
    version='1.0.0',
    packages=['cli_anything.metrics'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-metrics=cli_anything.metrics:cli']},
)
