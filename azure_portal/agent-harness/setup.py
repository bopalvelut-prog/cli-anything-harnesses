from setuptools import setup
setup(
    name='cli-anything-azure_portal',
    version='1.0.0',
    packages=['cli_anything.azure_portal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_portal=cli_anything.azure_portal:cli']},
)
