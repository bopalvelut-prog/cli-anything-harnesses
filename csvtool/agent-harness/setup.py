from setuptools import setup
setup(
    name='cli-anything-csvtool',
    version='1.0.0',
    packages=['cli_anything.csvtool'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-csvtool=cli_anything.csvtool:cli']},
)
