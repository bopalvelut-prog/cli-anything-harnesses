from setuptools import setup
setup(
    name='cli-anything-hetzner_action',
    version='1.0.0',
    packages=['cli_anything.hetzner_action'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_action=cli_anything.hetzner_action:cli']},
)
