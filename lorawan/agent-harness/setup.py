from setuptools import setup
setup(
    name='cli-anything-lorawan',
    version='1.0.0',
    packages=['cli_anything.lorawan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lorawan=cli_anything.lorawan:cli']},
)
