from setuptools import setup
setup(
    name='cli-anything-azure_bot',
    version='1.0.0',
    packages=['cli_anything.azure_bot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_bot=cli_anything.azure_bot:cli']},
)
