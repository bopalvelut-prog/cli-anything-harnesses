from setuptools import setup
setup(
    name='cli-anything-azure_powerbiembedded',
    version='1.0.0',
    packages=['cli_anything.azure_powerbiembedded'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_powerbiembedded=cli_anything.azure_powerbiembedded:cli']},
)
