from setuptools import setup
setup(
    name='cli-anything-azure_subscription',
    version='1.0.0',
    packages=['cli_anything.azure_subscription'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_subscription=cli_anything.azure_subscription:cli']},
)
