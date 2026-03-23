from setuptools import setup
setup(
    name='cli-anything-hetzner_server_type',
    version='1.0.0',
    packages=['cli_anything.hetzner_server_type'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_server_type=cli_anything.hetzner_server_type:cli']},
)
