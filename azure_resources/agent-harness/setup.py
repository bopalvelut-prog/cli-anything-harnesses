from setuptools import setup
setup(
    name='cli-anything-azure_resources',
    version='1.0.0',
    packages=['cli_anything.azure_resources'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_resources=cli_anything.azure_resources:cli']},
)
