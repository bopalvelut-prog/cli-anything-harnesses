from setuptools import setup
setup(
    name='cli-anything-azure_firmware',
    version='1.0.0',
    packages=['cli_anything.azure_firmware'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_firmware=cli_anything.azure_firmware:cli']},
)
