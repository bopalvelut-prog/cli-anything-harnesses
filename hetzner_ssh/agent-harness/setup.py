from setuptools import setup
setup(
    name='cli-anything-hetzner_ssh',
    version='1.0.0',
    packages=['cli_anything.hetzner_ssh'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_ssh=cli_anything.hetzner_ssh:cli']},
)
