from setuptools import setup
setup(
    name='cli-anything-azure_windowsiot',
    version='1.0.0',
    packages=['cli_anything.azure_windowsiot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_windowsiot=cli_anything.azure_windowsiot:cli']},
)
