from setuptools import setup
setup(
    name='cli-anything-azure_expressroute',
    version='1.0.0',
    packages=['cli_anything.azure_expressroute'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_expressroute=cli_anything.azure_expressroute:cli']},
)
