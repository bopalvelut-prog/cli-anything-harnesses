from setuptools import setup
setup(
    name='cli-anything-azure_avalanche',
    version='1.0.0',
    packages=['cli_anything.azure_avalanche'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_avalanche=cli_anything.azure_avalanche:cli']},
)
