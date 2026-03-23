from setuptools import setup
setup(
    name='cli-anything-azure_automation',
    version='1.0.0',
    packages=['cli_anything.azure_automation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_automation=cli_anything.azure_automation:cli']},
)
