from setuptools import setup
setup(
    name='cli-anything-odoo',
    version='1.0.0',
    packages=['cli_anything.odoo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-odoo=cli_anything.odoo:cli']},
)
