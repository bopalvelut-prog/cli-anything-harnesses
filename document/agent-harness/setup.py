from setuptools import setup
setup(
    name='cli-anything-document',
    version='1.0.0',
    packages=['cli_anything.document'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-document=cli_anything.document:cli']},
)
