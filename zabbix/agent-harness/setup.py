from setuptools import setup
setup(
    name='cli-anything-zabbix',
    version='1.0.0',
    packages=['cli_anything.zabbix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zabbix=cli_anything.zabbix:cli']},
)
