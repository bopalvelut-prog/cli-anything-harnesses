from setuptools import setup
setup(
    name='cli-anything-cloudflare_firewall',
    version='1.0.0',
    packages=['cli_anything.cloudflare_firewall'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_firewall=cli_anything.cloudflare_firewall:cli']},
)
