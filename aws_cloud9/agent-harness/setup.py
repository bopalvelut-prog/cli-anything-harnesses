from setuptools import setup
setup(
    name='cli-anything-aws_cloud9',
    version='1.0.0',
    packages=['cli_anything.aws_cloud9'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_cloud9=cli_anything.aws_cloud9:cli']},
)
