from setuptools import setup
setup(
    name='cli-anything-azure_iothub',
    version='1.0.0',
    packages=['cli_anything.azure_iothub'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_iothub=cli_anything.azure_iothub:cli']},
)
