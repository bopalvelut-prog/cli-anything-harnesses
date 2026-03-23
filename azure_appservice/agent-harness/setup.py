from setuptools import setup
setup(
    name='cli-anything-azure_appservice',
    version='1.0.0',
    packages=['cli_anything.azure_appservice'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_appservice=cli_anything.azure_appservice:cli']},
)
