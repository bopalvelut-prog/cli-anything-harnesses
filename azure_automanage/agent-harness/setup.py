from setuptools import setup
setup(
    name='cli-anything-azure_automanage',
    version='1.0.0',
    packages=['cli_anything.azure_automanage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_automanage=cli_anything.azure_automanage:cli']},
)
