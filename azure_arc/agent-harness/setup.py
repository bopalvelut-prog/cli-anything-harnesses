from setuptools import setup
setup(
    name='cli-anything-azure_arc',
    version='1.0.0',
    packages=['cli_anything.azure_arc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_arc=cli_anything.azure_arc:cli']},
)
