from setuptools import setup
setup(
    name='cli-anything-azure_streamanalytics',
    version='1.0.0',
    packages=['cli_anything.azure_streamanalytics'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_streamanalytics=cli_anything.azure_streamanalytics:cli']},
)
