from setuptools import setup
setup(
    name='cli-anything-azure_advisor',
    version='1.0.0',
    packages=['cli_anything.azure_advisor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_advisor=cli_anything.azure_advisor:cli']},
)
