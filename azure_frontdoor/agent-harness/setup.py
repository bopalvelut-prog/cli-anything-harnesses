from setuptools import setup
setup(
    name='cli-anything-azure_frontdoor',
    version='1.0.0',
    packages=['cli_anything.azure_frontdoor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_frontdoor=cli_anything.azure_frontdoor:cli']},
)
