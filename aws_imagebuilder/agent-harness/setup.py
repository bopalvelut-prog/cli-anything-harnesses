from setuptools import setup
setup(
    name='cli-anything-aws_imagebuilder',
    version='1.0.0',
    packages=['cli_anything.aws_imagebuilder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_imagebuilder=cli_anything.aws_imagebuilder:cli']},
)
