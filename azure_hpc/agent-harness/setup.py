from setuptools import setup
setup(
    name='cli-anything-azure_hpc',
    version='1.0.0',
    packages=['cli_anything.azure_hpc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_hpc=cli_anything.azure_hpc:cli']},
)
