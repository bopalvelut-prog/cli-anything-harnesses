from setuptools import setup
setup(
    name='cli-anything-azure_operationalinsights',
    version='1.0.0',
    packages=['cli_anything.azure_operationalinsights'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_operationalinsights=cli_anything.azure_operationalinsights:cli']},
)
