from setuptools import setup
setup(
    name='cli-anything-syslog',
    version='1.0.0',
    packages=['cli_anything.syslog'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-syslog=cli_anything.syslog:cli']},
)
