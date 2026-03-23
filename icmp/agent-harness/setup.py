from setuptools import setup
setup(
    name='cli-anything-icmp',
    version='1.0.0',
    packages=['cli_anything.icmp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-icmp=cli_anything.icmp:cli']},
)
