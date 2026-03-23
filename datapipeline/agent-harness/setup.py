from setuptools import setup
setup(
    name='cli-anything-datapipeline',
    version='1.0.0',
    packages=['cli_anything.datapipeline'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-datapipeline=cli_anything.datapipeline:cli']},
)
