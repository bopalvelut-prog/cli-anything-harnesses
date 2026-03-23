from setuptools import setup
setup(
    name='cli-anything-azure_purview',
    version='1.0.0',
    packages=['cli_anything.azure_purview'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_purview=cli_anything.azure_purview:cli']},
)
