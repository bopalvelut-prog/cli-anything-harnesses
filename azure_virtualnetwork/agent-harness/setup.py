from setuptools import setup
setup(
    name='cli-anything-azure_virtualnetwork',
    version='1.0.0',
    packages=['cli_anything.azure_virtualnetwork'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_virtualnetwork=cli_anything.azure_virtualnetwork:cli']},
)
