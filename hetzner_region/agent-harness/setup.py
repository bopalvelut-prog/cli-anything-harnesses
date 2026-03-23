from setuptools import setup
setup(
    name='cli-anything-hetzner_region',
    version='1.0.0',
    packages=['cli_anything.hetzner_region'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_region=cli_anything.hetzner_region:cli']},
)
