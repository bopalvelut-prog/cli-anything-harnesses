from setuptools import setup
setup(
    name='cli-anything-azure_spring',
    version='1.0.0',
    packages=['cli_anything.azure_spring'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_spring=cli_anything.azure_spring:cli']},
)
