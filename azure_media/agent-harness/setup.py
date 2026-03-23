from setuptools import setup
setup(
    name='cli-anything-azure_media',
    version='1.0.0',
    packages=['cli_anything.azure_media'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_media=cli_anything.azure_media:cli']},
)
