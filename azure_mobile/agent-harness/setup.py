from setuptools import setup
setup(
    name='cli-anything-azure_mobile',
    version='1.0.0',
    packages=['cli_anything.azure_mobile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_mobile=cli_anything.azure_mobile:cli']},
)
