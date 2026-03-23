from setuptools import setup
setup(
    name='cli-anything-azure_dedicatedhost',
    version='1.0.0',
    packages=['cli_anything.azure_dedicatedhost'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_dedicatedhost=cli_anything.azure_dedicatedhost:cli']},
)
