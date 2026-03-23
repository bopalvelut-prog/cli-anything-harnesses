from setuptools import setup
setup(
    name='cli-anything-azure_databox',
    version='1.0.0',
    packages=['cli_anything.azure_databox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_databox=cli_anything.azure_databox:cli']},
)
