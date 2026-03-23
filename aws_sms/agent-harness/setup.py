from setuptools import setup
setup(
    name='cli-anything-aws_sms',
    version='1.0.0',
    packages=['cli_anything.aws_sms'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_sms=cli_anything.aws_sms:cli']},
)
