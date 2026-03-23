from setuptools import setup
setup(
    name='cli-anything-azure_signalr',
    version='1.0.0',
    packages=['cli_anything.azure_signalr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_signalr=cli_anything.azure_signalr:cli']},
)
