from setuptools import setup
setup(
    name='cli-anything-azure_eventgrid',
    version='1.0.0',
    packages=['cli_anything.azure_eventgrid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_eventgrid=cli_anything.azure_eventgrid:cli']},
)
