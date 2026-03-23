from setuptools import setup
setup(
    name='cli-anything-bleve',
    version='1.0.0',
    packages=['cli_anything.bleve'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bleve=cli_anything.bleve:cli']},
)
