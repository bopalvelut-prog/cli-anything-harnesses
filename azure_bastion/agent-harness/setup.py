from setuptools import setup
setup(
    name='cli-anything-azure_bastion',
    version='1.0.0',
    packages=['cli_anything.azure_bastion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_bastion=cli_anything.azure_bastion:cli']},
)
