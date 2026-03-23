from setuptools import setup
setup(
    name='cli-anything-azure_postgresql',
    version='1.0.0',
    packages=['cli_anything.azure_postgresql'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_postgresql=cli_anything.azure_postgresql:cli']},
)
