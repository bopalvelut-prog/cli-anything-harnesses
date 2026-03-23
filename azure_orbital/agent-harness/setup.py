from setuptools import setup
setup(
    name='cli-anything-azure_orbital',
    version='1.0.0',
    packages=['cli_anything.azure_orbital'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_orbital=cli_anything.azure_orbital:cli']},
)
