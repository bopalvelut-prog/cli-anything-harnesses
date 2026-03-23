from setuptools import setup
setup(
    name='cli-anything-azure_cognitive',
    version='1.0.0',
    packages=['cli_anything.azure_cognitive'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_cognitive=cli_anything.azure_cognitive:cli']},
)
