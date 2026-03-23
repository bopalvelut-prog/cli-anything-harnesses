from setuptools import setup
setup(
    name='cli-anything-bert',
    version='1.0.0',
    packages=['cli_anything.bert'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bert=cli_anything.bert:cli']},
)
