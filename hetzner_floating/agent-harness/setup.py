from setuptools import setup
setup(
    name='cli-anything-hetzner_floating',
    version='1.0.0',
    packages=['cli_anything.hetzner_floating'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_floating=cli_anything.hetzner_floating:cli']},
)
