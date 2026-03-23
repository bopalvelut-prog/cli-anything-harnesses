from setuptools import setup
setup(
    name='cli-anything-dnsmasq',
    version='1.0.0',
    packages=['cli_anything.dnsmasq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dnsmasq=cli_anything.dnsmasq:cli']},
)
