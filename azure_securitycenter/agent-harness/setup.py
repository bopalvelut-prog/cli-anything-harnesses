from setuptools import setup
setup(
    name='cli-anything-azure_securitycenter',
    version='1.0.0',
    packages=['cli_anything.azure_securitycenter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_securitycenter=cli_anything.azure_securitycenter:cli']},
)
