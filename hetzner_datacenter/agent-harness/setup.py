from setuptools import setup
setup(
    name='cli-anything-hetzner_datacenter',
    version='1.0.0',
    packages=['cli_anything.hetzner_datacenter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_datacenter=cli_anything.hetzner_datacenter:cli']},
)
