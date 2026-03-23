from setuptools import setup
setup(
    name='cli-anything-nix',
    version='1.0.0',
    packages=['cli_anything.nix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nix=cli_anything.nix:cli']},
)
