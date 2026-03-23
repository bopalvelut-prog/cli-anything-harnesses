from setuptools import setup
setup(
    name='cli-anything-azure_monitor',
    version='1.0.0',
    packages=['cli_anything.azure_monitor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_monitor=cli_anything.azure_monitor:cli']},
)
