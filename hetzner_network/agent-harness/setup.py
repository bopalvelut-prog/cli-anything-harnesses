from setuptools import setup
setup(
    name='cli-anything-hetzner_network',
    version='1.0.0',
    packages=['cli_anything.hetzner_network'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_network=cli_anything.hetzner_network:cli']},
)
