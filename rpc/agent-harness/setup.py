from setuptools import setup
setup(
    name='cli-anything-rpc',
    version='1.0.0',
    packages=['cli_anything.rpc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rpc=cli_anything.rpc:cli']},
)
