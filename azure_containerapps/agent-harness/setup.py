from setuptools import setup
setup(
    name='cli-anything-azure_containerapps',
    version='1.0.0',
    packages=['cli_anything.azure_containerapps'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_containerapps=cli_anything.azure_containerapps:cli']},
)
