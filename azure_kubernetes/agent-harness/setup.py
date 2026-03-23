from setuptools import setup
setup(
    name='cli-anything-azure_kubernetes',
    version='1.0.0',
    packages=['cli_anything.azure_kubernetes'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_kubernetes=cli_anything.azure_kubernetes:cli']},
)
