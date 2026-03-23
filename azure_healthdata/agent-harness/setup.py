from setuptools import setup
setup(
    name='cli-anything-azure_healthdata',
    version='1.0.0',
    packages=['cli_anything.azure_healthdata'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_healthdata=cli_anything.azure_healthdata:cli']},
)
