from setuptools import setup
setup(
    name='cli-anything-hetzner_iso',
    version='1.0.0',
    packages=['cli_anything.hetzner_iso'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_iso=cli_anything.hetzner_iso:cli']},
)
