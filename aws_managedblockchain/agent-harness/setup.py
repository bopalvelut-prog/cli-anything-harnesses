from setuptools import setup
setup(
    name='cli-anything-aws_managedblockchain',
    version='1.0.0',
    packages=['cli_anything.aws_managedblockchain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_managedblockchain=cli_anything.aws_managedblockchain:cli']},
)
