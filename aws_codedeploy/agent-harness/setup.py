from setuptools import setup
setup(
    name='cli-anything-aws_codedeploy',
    version='1.0.0',
    packages=['cli_anything.aws_codedeploy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_codedeploy=cli_anything.aws_codedeploy:cli']},
)
