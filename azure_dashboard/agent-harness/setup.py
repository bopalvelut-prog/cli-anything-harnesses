from setuptools import setup
setup(
    name='cli-anything-azure_dashboard',
    version='1.0.0',
    packages=['cli_anything.azure_dashboard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_dashboard=cli_anything.azure_dashboard:cli']},
)
