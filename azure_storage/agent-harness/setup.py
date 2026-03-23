from setuptools import setup
setup(
    name='cli-anything-azure_storage',
    version='1.0.0',
    packages=['cli_anything.azure_storage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_storage=cli_anything.azure_storage:cli']},
)
