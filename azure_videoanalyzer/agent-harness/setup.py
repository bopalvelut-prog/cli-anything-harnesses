from setuptools import setup
setup(
    name='cli-anything-azure_videoanalyzer',
    version='1.0.0',
    packages=['cli_anything.azure_videoanalyzer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_videoanalyzer=cli_anything.azure_videoanalyzer:cli']},
)
