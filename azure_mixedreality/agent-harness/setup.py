from setuptools import setup
setup(
    name='cli-anything-azure_mixedreality',
    version='1.0.0',
    packages=['cli_anything.azure_mixedreality'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_mixedreality=cli_anything.azure_mixedreality:cli']},
)
