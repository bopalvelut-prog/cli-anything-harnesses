from setuptools import setup
setup(
    name='cli-anything-azure_machinelearning',
    version='1.0.0',
    packages=['cli_anything.azure_machinelearning'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_machinelearning=cli_anything.azure_machinelearning:cli']},
)
