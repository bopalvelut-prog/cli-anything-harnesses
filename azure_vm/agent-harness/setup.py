from setuptools import setup
setup(
    name='cli-anything-azure_vm',
    version='1.0.0',
    packages=['cli_anything.azure_vm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_vm=cli_anything.azure_vm:cli']},
)
