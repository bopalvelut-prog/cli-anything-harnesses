from setuptools import setup
setup(
    name='cli-anything-tcpdump',
    version='1.0.0',
    packages=['cli_anything.tcpdump'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tcpdump=cli_anything.tcpdump:cli']},
)
