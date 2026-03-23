from setuptools import setup
setup(
    name='cli-anything-azure_dataexplorer',
    version='1.0.0',
    packages=['cli_anything.azure_dataexplorer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_dataexplorer=cli_anything.azure_dataexplorer:cli']},
)
