from setuptools import setup
setup(
    name='cli-anything-brendangregg',
    version='1.0.0',
    packages=['cli_anything.brendangregg'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brendangregg=cli_anything.brendangregg:cli']},
)
