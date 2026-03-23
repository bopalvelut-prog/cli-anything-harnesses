from setuptools import setup
setup(
    name='cli-anything-sops',
    version='1.0.0',
    packages=['cli_anything.sops'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sops=cli_anything.sops:cli']},
)
