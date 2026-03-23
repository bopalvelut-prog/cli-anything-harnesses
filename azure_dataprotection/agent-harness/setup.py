from setuptools import setup
setup(
    name='cli-anything-azure_dataprotection',
    version='1.0.0',
    packages=['cli_anything.azure_dataprotection'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_dataprotection=cli_anything.azure_dataprotection:cli']},
)
