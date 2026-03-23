from setuptools import setup
setup(
    name='cli-anything-opentsdb',
    version='1.0.0',
    packages=['cli_anything.opentsdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-opentsdb=cli_anything.opentsdb:cli']},
)
