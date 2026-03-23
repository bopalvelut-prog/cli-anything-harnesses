from setuptools import setup
setup(
    name='cli-anything-aws_groundtruth',
    version='1.0.0',
    packages=['cli_anything.aws_groundtruth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_groundtruth=cli_anything.aws_groundtruth:cli']},
)
