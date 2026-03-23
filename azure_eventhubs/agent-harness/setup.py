from setuptools import setup
setup(
    name='cli-anything-azure_eventhubs',
    version='1.0.0',
    packages=['cli_anything.azure_eventhubs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_eventhubs=cli_anything.azure_eventhubs:cli']},
)
