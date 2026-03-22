from setuptools import setup
setup(
    name='cli-anything-veracode',
    version='1.0.0',
    packages=['cli_anything.veracode'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-veracode=cli_anything.veracode:cli']},
)
