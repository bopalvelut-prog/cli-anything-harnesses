from setuptools import setup
setup(
    name='cli-anything-azure_lighthouse',
    version='1.0.0',
    packages=['cli_anything.azure_lighthouse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_lighthouse=cli_anything.azure_lighthouse:cli']},
)
