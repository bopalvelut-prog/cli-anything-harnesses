from setuptools import setup
setup(
    name='cli-anything-azure_deploymentmanager',
    version='1.0.0',
    packages=['cli_anything.azure_deploymentmanager'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_deploymentmanager=cli_anything.azure_deploymentmanager:cli']},
)
