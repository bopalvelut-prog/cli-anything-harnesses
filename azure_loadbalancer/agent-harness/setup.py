from setuptools import setup
setup(
    name='cli-anything-azure_loadbalancer',
    version='1.0.0',
    packages=['cli_anything.azure_loadbalancer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_loadbalancer=cli_anything.azure_loadbalancer:cli']},
)
