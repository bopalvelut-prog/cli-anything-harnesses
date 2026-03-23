from setuptools import setup
setup(
    name='cli-anything-azure_support',
    version='1.0.0',
    packages=['cli_anything.azure_support'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_support=cli_anything.azure_support:cli']},
)
