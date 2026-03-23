from setuptools import setup
setup(
    name='cli-anything-cloud_foundry',
    version='1.0.0',
    packages=['cli_anything.cloud_foundry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloud_foundry=cli_anything.cloud_foundry:cli']},
)
