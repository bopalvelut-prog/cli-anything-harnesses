from setuptools import setup
setup(
    name='cli-anything-azure_sqlmanagedinstance',
    version='1.0.0',
    packages=['cli_anything.azure_sqlmanagedinstance'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_sqlmanagedinstance=cli_anything.azure_sqlmanagedinstance:cli']},
)
