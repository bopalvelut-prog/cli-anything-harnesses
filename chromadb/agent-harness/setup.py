from setuptools import setup
setup(
    name='cli-anything-chromadb',
    version='1.0.0',
    packages=['cli_anything.chromadb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chromadb=cli_anything.chromadb:cli']},
)
