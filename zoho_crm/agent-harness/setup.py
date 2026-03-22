from setuptools import setup
setup(
    name='cli-anything-zoho_crm',
    version='1.0.0',
    packages=['cli_anything.zoho_crm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zoho_crm=cli_anything.zoho_crm:cli']},
)
