from setuptools import setup
setup(
    name='cli-anything-azure_tables',
    version='1.0.0',
    packages=['cli_anything.azure_tables'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_tables=cli_anything.azure_tables:cli']},
)
