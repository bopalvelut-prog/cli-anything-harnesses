from setuptools import setup
setup(
    name='cli-anything-azure_iotsecurity',
    version='1.0.0',
    packages=['cli_anything.azure_iotsecurity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_iotsecurity=cli_anything.azure_iotsecurity:cli']},
)
