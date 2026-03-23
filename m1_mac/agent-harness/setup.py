from setuptools import setup
setup(
    name='cli-anything-m1_mac',
    version='1.0.0',
    packages=['cli_anything.m1_mac'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-m1_mac=cli_anything.m1_mac:cli']},
)
