from setuptools import setup
setup(
    name='cli-anything-azure_functions',
    version='1.0.0',
    packages=['cli_anything.azure_functions'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_functions=cli_anything.azure_functions:cli']},
)
