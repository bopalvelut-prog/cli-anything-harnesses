from setuptools import setup
setup(
    name='cli-anything-azure_databricks',
    version='1.0.0',
    packages=['cli_anything.azure_databricks'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_databricks=cli_anything.azure_databricks:cli']},
)
