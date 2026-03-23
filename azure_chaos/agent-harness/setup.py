from setuptools import setup
setup(
    name='cli-anything-azure_chaos',
    version='1.0.0',
    packages=['cli_anything.azure_chaos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_chaos=cli_anything.azure_chaos:cli']},
)
