from setuptools import setup
setup(
    name='cli-anything-azure_kusto',
    version='1.0.0',
    packages=['cli_anything.azure_kusto'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_kusto=cli_anything.azure_kusto:cli']},
)
