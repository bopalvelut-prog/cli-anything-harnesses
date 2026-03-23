from setuptools import setup
setup(
    name='cli-anything-azure_mysql',
    version='1.0.0',
    packages=['cli_anything.azure_mysql'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_mysql=cli_anything.azure_mysql:cli']},
)
