from setuptools import setup
setup(
    name='cli-anything-zstd',
    version='1.0.0',
    packages=['cli_anything.zstd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zstd=cli_anything.zstd:cli']},
)
