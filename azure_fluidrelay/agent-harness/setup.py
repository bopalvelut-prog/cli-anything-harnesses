from setuptools import setup
setup(
    name='cli-anything-azure_fluidrelay',
    version='1.0.0',
    packages=['cli_anything.azure_fluidrelay'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_fluidrelay=cli_anything.azure_fluidrelay:cli']},
)
