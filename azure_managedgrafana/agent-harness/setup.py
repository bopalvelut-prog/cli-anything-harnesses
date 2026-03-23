from setuptools import setup
setup(
    name='cli-anything-azure_managedgrafana',
    version='1.0.0',
    packages=['cli_anything.azure_managedgrafana'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_managedgrafana=cli_anything.azure_managedgrafana:cli']},
)
