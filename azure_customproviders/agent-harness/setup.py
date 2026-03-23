from setuptools import setup
setup(
    name='cli-anything-azure_customproviders',
    version='1.0.0',
    packages=['cli_anything.azure_customproviders'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_customproviders=cli_anything.azure_customproviders:cli']},
)
