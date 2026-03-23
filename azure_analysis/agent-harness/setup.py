from setuptools import setup
setup(
    name='cli-anything-azure_analysis',
    version='1.0.0',
    packages=['cli_anything.azure_analysis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_analysis=cli_anything.azure_analysis:cli']},
)
