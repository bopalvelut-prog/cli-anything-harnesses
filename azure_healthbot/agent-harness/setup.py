from setuptools import setup
setup(
    name='cli-anything-azure_healthbot',
    version='1.0.0',
    packages=['cli_anything.azure_healthbot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_healthbot=cli_anything.azure_healthbot:cli']},
)
