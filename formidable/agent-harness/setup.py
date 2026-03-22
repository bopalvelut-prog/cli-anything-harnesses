from setuptools import setup
setup(
    name='cli-anything-formidable',
    version='1.0.0',
    packages=['cli_anything.formidable'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-formidable=cli_anything.formidable:cli']},
)
