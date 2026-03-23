from setuptools import setup
setup(
    name='cli-anything-openfga',
    version='1.0.0',
    packages=['cli_anything.openfga'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openfga=cli_anything.openfga:cli']},
)
