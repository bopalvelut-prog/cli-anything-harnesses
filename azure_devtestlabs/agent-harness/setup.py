from setuptools import setup
setup(
    name='cli-anything-azure_devtestlabs',
    version='1.0.0',
    packages=['cli_anything.azure_devtestlabs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_devtestlabs=cli_anything.azure_devtestlabs:cli']},
)
