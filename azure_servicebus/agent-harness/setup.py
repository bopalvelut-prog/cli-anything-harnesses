from setuptools import setup
setup(
    name='cli-anything-azure_servicebus',
    version='1.0.0',
    packages=['cli_anything.azure_servicebus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_servicebus=cli_anything.azure_servicebus:cli']},
)
