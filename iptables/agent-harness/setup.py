from setuptools import setup
setup(
    name='cli-anything-iptables',
    version='1.0.0',
    packages=['cli_anything.iptables'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-iptables=cli_anything.iptables:cli']},
)
