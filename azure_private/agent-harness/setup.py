from setuptools import setup
setup(
    name='cli-anything-azure_private',
    version='1.0.0',
    packages=['cli_anything.azure_private'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_private=cli_anything.azure_private:cli']},
)
