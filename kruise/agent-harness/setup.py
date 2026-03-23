from setuptools import setup
setup(
    name='cli-anything-kruise',
    version='1.0.0',
    packages=['cli_anything.kruise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kruise=cli_anything.kruise:cli']},
)
