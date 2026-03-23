from setuptools import setup
setup(
    name='cli-anything-aws_memorydb',
    version='1.0.0',
    packages=['cli_anything.aws_memorydb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_memorydb=cli_anything.aws_memorydb:cli']},
)
