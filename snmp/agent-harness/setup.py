from setuptools import setup
setup(
    name='cli-anything-snmp',
    version='1.0.0',
    packages=['cli_anything.snmp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-snmp=cli_anything.snmp:cli']},
)
