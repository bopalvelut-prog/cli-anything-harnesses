from setuptools import setup
setup(
    name='cli-anything-azure_keyvault',
    version='1.0.0',
    packages=['cli_anything.azure_keyvault'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_keyvault=cli_anything.azure_keyvault:cli']},
)
