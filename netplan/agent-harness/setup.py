from setuptools import setup
setup(
    name='cli-anything-netplan',
    version='1.0.0',
    packages=['cli_anything.netplan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-netplan=cli_anything.netplan:cli']},
)
