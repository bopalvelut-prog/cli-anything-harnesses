from setuptools import setup
setup(
    name='cli-anything-azure_powerbidedicated',
    version='1.0.0',
    packages=['cli_anything.azure_powerbidedicated'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_powerbidedicated=cli_anything.azure_powerbidedicated:cli']},
)
