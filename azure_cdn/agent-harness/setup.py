from setuptools import setup
setup(
    name='cli-anything-azure_cdn',
    version='1.0.0',
    packages=['cli_anything.azure_cdn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_cdn=cli_anything.azure_cdn:cli']},
)
