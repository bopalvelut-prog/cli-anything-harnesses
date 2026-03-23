from setuptools import setup
setup(
    name='cli-anything-hetzner_snapshot',
    version='1.0.0',
    packages=['cli_anything.hetzner_snapshot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_snapshot=cli_anything.hetzner_snapshot:cli']},
)
