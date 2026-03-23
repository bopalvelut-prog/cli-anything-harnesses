from setuptools import setup
setup(
    name='cli-anything-azure_dns',
    version='1.0.0',
    packages=['cli_anything.azure_dns'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_dns=cli_anything.azure_dns:cli']},
)
