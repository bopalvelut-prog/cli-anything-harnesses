from setuptools import setup
setup(
    name='cli-anything-hetzner_firewall',
    version='1.0.0',
    packages=['cli_anything.hetzner_firewall'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_firewall=cli_anything.hetzner_firewall:cli']},
)
