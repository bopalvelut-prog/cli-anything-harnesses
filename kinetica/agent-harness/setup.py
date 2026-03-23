from setuptools import setup
setup(
    name='cli-anything-kinetica',
    version='1.0.0',
    packages=['cli_anything.kinetica'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kinetica=cli_anything.kinetica:cli']},
)
