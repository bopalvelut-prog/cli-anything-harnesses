from setuptools import setup
setup(
    name='cli-anything-azure_appconfiguration',
    version='1.0.0',
    packages=['cli_anything.azure_appconfiguration'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_appconfiguration=cli_anything.azure_appconfiguration:cli']},
)
