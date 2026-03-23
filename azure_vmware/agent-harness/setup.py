from setuptools import setup
setup(
    name='cli-anything-azure_vmware',
    version='1.0.0',
    packages=['cli_anything.azure_vmware'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_vmware=cli_anything.azure_vmware:cli']},
)
