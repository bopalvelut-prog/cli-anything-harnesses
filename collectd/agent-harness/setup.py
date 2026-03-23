from setuptools import setup
setup(
    name='cli-anything-collectd',
    version='1.0.0',
    packages=['cli_anything.collectd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-collectd=cli_anything.collectd:cli']},
)
