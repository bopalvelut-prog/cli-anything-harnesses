from setuptools import setup
setup(
    name='cli-anything-azure_apimanagement',
    version='1.0.0',
    packages=['cli_anything.azure_apimanagement'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_apimanagement=cli_anything.azure_apimanagement:cli']},
)
