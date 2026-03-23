from setuptools import setup
setup(
    name='cli-anything-azure_hdinsight',
    version='1.0.0',
    packages=['cli_anything.azure_hdinsight'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_hdinsight=cli_anything.azure_hdinsight:cli']},
)
