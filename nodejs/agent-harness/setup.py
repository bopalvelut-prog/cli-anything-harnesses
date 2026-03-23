from setuptools import setup
setup(
    name='cli-anything-nodejs',
    version='1.0.0',
    packages=['cli_anything.nodejs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nodejs=cli_anything.nodejs:cli']},
)
