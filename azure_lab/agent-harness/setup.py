from setuptools import setup
setup(
    name='cli-anything-azure_lab',
    version='1.0.0',
    packages=['cli_anything.azure_lab'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_lab=cli_anything.azure_lab:cli']},
)
