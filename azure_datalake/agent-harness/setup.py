from setuptools import setup
setup(
    name='cli-anything-azure_datalake',
    version='1.0.0',
    packages=['cli_anything.azure_datalake'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_datalake=cli_anything.azure_datalake:cli']},
)
