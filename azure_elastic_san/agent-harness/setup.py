from setuptools import setup
setup(
    name='cli-anything-azure_elastic_san',
    version='1.0.0',
    packages=['cli_anything.azure_elastic_san'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_elastic_san=cli_anything.azure_elastic_san:cli']},
)
