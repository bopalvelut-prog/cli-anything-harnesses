from setuptools import setup
setup(
    name='cli-anything-aws_storage_gateway',
    version='1.0.0',
    packages=['cli_anything.aws_storage_gateway'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_storage_gateway=cli_anything.aws_storage_gateway:cli']},
)
