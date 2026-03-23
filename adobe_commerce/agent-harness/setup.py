from setuptools import setup
setup(
    name='cli-anything-adobe_commerce',
    version='1.0.0',
    packages=['cli_anything.adobe_commerce'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-adobe_commerce=cli_anything.adobe_commerce:cli']},
)
