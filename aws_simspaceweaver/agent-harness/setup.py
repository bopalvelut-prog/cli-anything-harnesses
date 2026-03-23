from setuptools import setup
setup(
    name='cli-anything-aws_simspaceweaver',
    version='1.0.0',
    packages=['cli_anything.aws_simspaceweaver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_simspaceweaver=cli_anything.aws_simspaceweaver:cli']},
)
