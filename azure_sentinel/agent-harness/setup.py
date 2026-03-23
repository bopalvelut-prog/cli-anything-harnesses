from setuptools import setup
setup(
    name='cli-anything-azure_sentinel',
    version='1.0.0',
    packages=['cli_anything.azure_sentinel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_sentinel=cli_anything.azure_sentinel:cli']},
)
