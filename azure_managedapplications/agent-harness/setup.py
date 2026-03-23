from setuptools import setup
setup(
    name='cli-anything-azure_managedapplications',
    version='1.0.0',
    packages=['cli_anything.azure_managedapplications'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_managedapplications=cli_anything.azure_managedapplications:cli']},
)
