from setuptools import setup
setup(
    name='cli-anything-azure_config',
    version='1.0.0',
    packages=['cli_anything.azure_config'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_config=cli_anything.azure_config:cli']},
)
