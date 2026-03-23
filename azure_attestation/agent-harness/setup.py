from setuptools import setup
setup(
    name='cli-anything-azure_attestation',
    version='1.0.0',
    packages=['cli_anything.azure_attestation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_attestation=cli_anything.azure_attestation:cli']},
)
