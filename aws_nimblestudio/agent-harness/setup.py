from setuptools import setup
setup(
    name='cli-anything-aws_nimblestudio',
    version='1.0.0',
    packages=['cli_anything.aws_nimblestudio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_nimblestudio=cli_anything.aws_nimblestudio:cli']},
)
