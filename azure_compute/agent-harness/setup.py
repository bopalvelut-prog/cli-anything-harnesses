from setuptools import setup
setup(
    name='cli-anything-azure_compute',
    version='1.0.0',
    packages=['cli_anything.azure_compute'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_compute=cli_anything.azure_compute:cli']},
)
