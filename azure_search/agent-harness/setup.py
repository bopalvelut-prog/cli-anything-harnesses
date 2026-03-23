from setuptools import setup
setup(
    name='cli-anything-azure_search',
    version='1.0.0',
    packages=['cli_anything.azure_search'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_search=cli_anything.azure_search:cli']},
)
