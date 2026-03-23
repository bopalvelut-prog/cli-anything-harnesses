from setuptools import setup
setup(
    name='cli-anything-smartcontract',
    version='1.0.0',
    packages=['cli_anything.smartcontract'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-smartcontract=cli_anything.smartcontract:cli']},
)
