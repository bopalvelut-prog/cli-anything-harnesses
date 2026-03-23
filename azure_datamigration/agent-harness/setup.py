from setuptools import setup
setup(
    name='cli-anything-azure_datamigration',
    version='1.0.0',
    packages=['cli_anything.azure_datamigration'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_datamigration=cli_anything.azure_datamigration:cli']},
)
