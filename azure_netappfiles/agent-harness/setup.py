from setuptools import setup
setup(
    name='cli-anything-azure_netappfiles',
    version='1.0.0',
    packages=['cli_anything.azure_netappfiles'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_netappfiles=cli_anything.azure_netappfiles:cli']},
)
