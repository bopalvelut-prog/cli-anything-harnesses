from setuptools import setup
setup(
    name='cli-anything-azure_saas',
    version='1.0.0',
    packages=['cli_anything.azure_saas'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_saas=cli_anything.azure_saas:cli']},
)
