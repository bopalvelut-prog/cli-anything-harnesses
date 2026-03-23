from setuptools import setup
setup(
    name='cli-anything-datafusion',
    version='1.0.0',
    packages=['cli_anything.datafusion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-datafusion=cli_anything.datafusion:cli']},
)
