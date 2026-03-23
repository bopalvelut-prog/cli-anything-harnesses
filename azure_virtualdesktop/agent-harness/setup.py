from setuptools import setup
setup(
    name='cli-anything-azure_virtualdesktop',
    version='1.0.0',
    packages=['cli_anything.azure_virtualdesktop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_virtualdesktop=cli_anything.azure_virtualdesktop:cli']},
)
