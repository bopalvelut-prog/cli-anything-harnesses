from setuptools import setup
setup(
    name='cli-anything-nftport',
    version='1.0.0',
    packages=['cli_anything.nftport'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nftport=cli_anything.nftport:cli']},
)
