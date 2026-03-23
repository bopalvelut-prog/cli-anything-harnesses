from setuptools import setup
setup(
    name='cli-anything-hetzner_stats',
    version='1.0.0',
    packages=['cli_anything.hetzner_stats'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_stats=cli_anything.hetzner_stats:cli']},
)
