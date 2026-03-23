from setuptools import setup
setup(
    name='cli-anything-azure_network',
    version='1.0.0',
    packages=['cli_anything.azure_network'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_network=cli_anything.azure_network:cli']},
)
