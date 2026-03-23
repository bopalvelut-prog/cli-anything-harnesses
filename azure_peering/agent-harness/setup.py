from setuptools import setup
setup(
    name='cli-anything-azure_peering',
    version='1.0.0',
    packages=['cli_anything.azure_peering'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_peering=cli_anything.azure_peering:cli']},
)
