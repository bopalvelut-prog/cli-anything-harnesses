from setuptools import setup
setup(
    name='cli-anything-azure_siterecovery',
    version='1.0.0',
    packages=['cli_anything.azure_siterecovery'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_siterecovery=cli_anything.azure_siterecovery:cli']},
)
