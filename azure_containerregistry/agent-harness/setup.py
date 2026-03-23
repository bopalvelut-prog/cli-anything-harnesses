from setuptools import setup
setup(
    name='cli-anything-azure_containerregistry',
    version='1.0.0',
    packages=['cli_anything.azure_containerregistry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_containerregistry=cli_anything.azure_containerregistry:cli']},
)
