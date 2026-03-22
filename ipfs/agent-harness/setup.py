from setuptools import setup
setup(
    name='cli-anything-ipfs',
    version='1.0.0',
    packages=['cli_anything.ipfs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ipfs=cli_anything.ipfs:cli']},
)
