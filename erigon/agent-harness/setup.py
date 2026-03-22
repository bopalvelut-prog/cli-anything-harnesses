from setuptools import setup
setup(
    name='cli-anything-erigon',
    version='1.0.0',
    packages=['cli_anything.erigon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-erigon=cli_anything.erigon:cli']},
)
