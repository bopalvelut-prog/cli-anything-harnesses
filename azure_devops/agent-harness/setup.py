from setuptools import setup
setup(
    name='cli-anything-azure_devops',
    version='1.0.0',
    packages=['cli_anything.azure_devops'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_devops=cli_anything.azure_devops:cli']},
)
