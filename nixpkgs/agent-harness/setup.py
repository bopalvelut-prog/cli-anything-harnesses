from setuptools import setup
setup(
    name='cli-anything-nixpkgs',
    version='1.0.0',
    packages=['cli_anything.nixpkgs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nixpkgs=cli_anything.nixpkgs:cli']},
)
