from setuptools import setup
setup(
    name='cli-anything-rocksdb',
    version='1.0.0',
    packages=['cli_anything.rocksdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rocksdb=cli_anything.rocksdb:cli']},
)
