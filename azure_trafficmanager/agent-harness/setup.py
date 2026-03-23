from setuptools import setup
setup(
    name='cli-anything-azure_trafficmanager',
    version='1.0.0',
    packages=['cli_anything.azure_trafficmanager'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_trafficmanager=cli_anything.azure_trafficmanager:cli']},
)
