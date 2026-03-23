from setuptools import setup
setup(
    name='cli-anything-azure_relay',
    version='1.0.0',
    packages=['cli_anything.azure_relay'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_relay=cli_anything.azure_relay:cli']},
)
