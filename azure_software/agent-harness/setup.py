from setuptools import setup
setup(
    name='cli-anything-azure_software',
    version='1.0.0',
    packages=['cli_anything.azure_software'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_software=cli_anything.azure_software:cli']},
)
