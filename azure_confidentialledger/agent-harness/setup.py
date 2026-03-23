from setuptools import setup
setup(
    name='cli-anything-azure_confidentialledger',
    version='1.0.0',
    packages=['cli_anything.azure_confidentialledger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_confidentialledger=cli_anything.azure_confidentialledger:cli']},
)
