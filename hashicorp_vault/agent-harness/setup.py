from setuptools import setup
setup(
    name='cli-anything-hashicorp_vault',
    version='1.0.0',
    packages=['cli_anything.hashicorp_vault'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hashicorp_vault=cli_anything.hashicorp_vault:cli']},
)
