from setuptools import setup
setup(
    name='cli-anything-hetzner_load',
    version='1.0.0',
    packages=['cli_anything.hetzner_load'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_load=cli_anything.hetzner_load:cli']},
)
