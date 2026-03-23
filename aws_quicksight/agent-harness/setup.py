from setuptools import setup
setup(
    name='cli-anything-aws_quicksight',
    version='1.0.0',
    packages=['cli_anything.aws_quicksight'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_quicksight=cli_anything.aws_quicksight:cli']},
)
