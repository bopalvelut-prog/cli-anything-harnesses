from setuptools import setup
setup(
    name='cli-anything-aws_eventbridge',
    version='1.0.0',
    packages=['cli_anything.aws_eventbridge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_eventbridge=cli_anything.aws_eventbridge:cli']},
)
