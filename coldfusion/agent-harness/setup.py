from setuptools import setup
setup(
    name='cli-anything-coldfusion',
    version='1.0.0',
    packages=['cli_anything.coldfusion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coldfusion=cli_anything.coldfusion:cli']},
)
