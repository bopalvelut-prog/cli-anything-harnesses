from setuptools import setup
setup(
    name='cli-anything-aws_cloudhsm',
    version='1.0.0',
    packages=['cli_anything.aws_cloudhsm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_cloudhsm=cli_anything.aws_cloudhsm:cli']},
)
