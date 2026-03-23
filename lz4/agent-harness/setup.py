from setuptools import setup
setup(
    name='cli-anything-lz4',
    version='1.0.0',
    packages=['cli_anything.lz4'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lz4=cli_anything.lz4:cli']},
)
