from setuptools import setup
setup(
    name='cli-anything-azure_webpubsub',
    version='1.0.0',
    packages=['cli_anything.azure_webpubsub'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_webpubsub=cli_anything.azure_webpubsub:cli']},
)
