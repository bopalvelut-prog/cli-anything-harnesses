from setuptools import setup
setup(
    name='cli-anything-aws_eks',
    version='1.0.0',
    packages=['cli_anything.aws_eks'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_eks=cli_anything.aws_eks:cli']},
)
