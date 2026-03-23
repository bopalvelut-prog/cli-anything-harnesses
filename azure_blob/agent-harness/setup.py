from setuptools import setup
setup(
    name='cli-anything-azure_blob',
    version='1.0.0',
    packages=['cli_anything.azure_blob'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_blob=cli_anything.azure_blob:cli']},
)
