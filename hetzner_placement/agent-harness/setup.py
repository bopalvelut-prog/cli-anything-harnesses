from setuptools import setup
setup(
    name='cli-anything-hetzner_placement',
    version='1.0.0',
    packages=['cli_anything.hetzner_placement'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_placement=cli_anything.hetzner_placement:cli']},
)
