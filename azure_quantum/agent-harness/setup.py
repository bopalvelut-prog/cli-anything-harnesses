from setuptools import setup
setup(
    name='cli-anything-azure_quantum',
    version='1.0.0',
    packages=['cli_anything.azure_quantum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_quantum=cli_anything.azure_quantum:cli']},
)
