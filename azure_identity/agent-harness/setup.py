from setuptools import setup
setup(
    name='cli-anything-azure_identity',
    version='1.0.0',
    packages=['cli_anything.azure_identity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_identity=cli_anything.azure_identity:cli']},
)
