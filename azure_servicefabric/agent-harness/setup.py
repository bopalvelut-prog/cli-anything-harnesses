from setuptools import setup
setup(
    name='cli-anything-azure_servicefabric',
    version='1.0.0',
    packages=['cli_anything.azure_servicefabric'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_servicefabric=cli_anything.azure_servicefabric:cli']},
)
