from setuptools import setup
setup(
    name='cli-anything-aws_wellarchitected',
    version='1.0.0',
    packages=['cli_anything.aws_wellarchitected'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_wellarchitected=cli_anything.aws_wellarchitected:cli']},
)
