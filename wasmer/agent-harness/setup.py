from setuptools import setup
setup(
    name='cli-anything-wasmer',
    version='1.0.0',
    packages=['cli_anything.wasmer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wasmer=cli_anything.wasmer:cli']},
)
