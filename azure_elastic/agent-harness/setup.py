from setuptools import setup
setup(
    name='cli-anything-azure_elastic',
    version='1.0.0',
    packages=['cli_anything.azure_elastic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_elastic=cli_anything.azure_elastic:cli']},
)
