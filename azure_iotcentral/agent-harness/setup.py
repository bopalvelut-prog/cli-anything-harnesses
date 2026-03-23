from setuptools import setup
setup(
    name='cli-anything-azure_iotcentral',
    version='1.0.0',
    packages=['cli_anything.azure_iotcentral'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_iotcentral=cli_anything.azure_iotcentral:cli']},
)
