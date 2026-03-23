from setuptools import setup
setup(
    name='cli-anything-hetzner_action2',
    version='1.0.0',
    packages=['cli_anything.hetzner_action2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_action2=cli_anything.hetzner_action2:cli']},
)
