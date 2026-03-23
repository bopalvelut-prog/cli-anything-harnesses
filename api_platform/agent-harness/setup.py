from setuptools import setup
setup(
    name='cli-anything-api_platform',
    version='1.0.0',
    packages=['cli_anything.api_platform'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-api_platform=cli_anything.api_platform:cli']},
)
