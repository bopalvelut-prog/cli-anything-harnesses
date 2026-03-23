from setuptools import setup
setup(
    name='cli-anything-acumatica',
    version='1.0.0',
    packages=['cli_anything.acumatica'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-acumatica=cli_anything.acumatica:cli']},
)
