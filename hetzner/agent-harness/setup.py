from setuptools import setup
setup(
    name='cli-anything-hetzner',
    version='1.0.0',
    packages=['cli_anything.hetzner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner=cli_anything.hetzner:cli']},
)
