from setuptools import setup
setup(
    name='cli-anything-azure_policy',
    version='1.0.0',
    packages=['cli_anything.azure_policy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_policy=cli_anything.azure_policy:cli']},
)
