from setuptools import setup
setup(
    name='cli-anything-azure_logicapps',
    version='1.0.0',
    packages=['cli_anything.azure_logicapps'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_logicapps=cli_anything.azure_logicapps:cli']},
)
