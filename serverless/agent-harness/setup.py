from setuptools import setup
setup(
    name='cli-anything-serverless',
    version='1.0.0',
    packages=['cli_anything.serverless'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-serverless=cli_anything.serverless:cli']},
)
