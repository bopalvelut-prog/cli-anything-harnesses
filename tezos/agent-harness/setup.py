from setuptools import setup
setup(
    name='cli-anything-tezos',
    version='1.0.0',
    packages=['cli_anything.tezos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tezos=cli_anything.tezos:cli']},
)
