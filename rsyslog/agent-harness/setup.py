from setuptools import setup
setup(
    name='cli-anything-rsyslog',
    version='1.0.0',
    packages=['cli_anything.rsyslog'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rsyslog=cli_anything.rsyslog:cli']},
)
