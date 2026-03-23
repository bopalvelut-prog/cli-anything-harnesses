from setuptools import setup
setup(
    name='cli-anything-hetzner_location',
    version='1.0.0',
    packages=['cli_anything.hetzner_location'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_location=cli_anything.hetzner_location:cli']},
)
