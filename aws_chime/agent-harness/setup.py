from setuptools import setup
setup(
    name='cli-anything-aws_chime',
    version='1.0.0',
    packages=['cli_anything.aws_chime'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_chime=cli_anything.aws_chime:cli']},
)
