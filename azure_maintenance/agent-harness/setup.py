from setuptools import setup
setup(
    name='cli-anything-azure_maintenance',
    version='1.0.0',
    packages=['cli_anything.azure_maintenance'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_maintenance=cli_anything.azure_maintenance:cli']},
)
