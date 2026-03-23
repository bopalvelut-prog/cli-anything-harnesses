from setuptools import setup
setup(
    name='cli-anything-chunking',
    version='1.0.0',
    packages=['cli_anything.chunking'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chunking=cli_anything.chunking:cli']},
)
