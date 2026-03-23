from setuptools import setup
setup(
    name='cli-anything-azure_billing',
    version='1.0.0',
    packages=['cli_anything.azure_billing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_billing=cli_anything.azure_billing:cli']},
)
