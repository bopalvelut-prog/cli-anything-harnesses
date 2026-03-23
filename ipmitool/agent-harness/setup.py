from setuptools import setup
setup(
    name='cli-anything-ipmitool',
    version='1.0.0',
    packages=['cli_anything.ipmitool'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ipmitool=cli_anything.ipmitool:cli']},
)
