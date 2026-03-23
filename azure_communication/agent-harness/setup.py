from setuptools import setup
setup(
    name='cli-anything-azure_communication',
    version='1.0.0',
    packages=['cli_anything.azure_communication'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_communication=cli_anything.azure_communication:cli']},
)
