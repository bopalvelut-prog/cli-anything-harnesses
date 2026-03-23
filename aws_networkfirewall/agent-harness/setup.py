from setuptools import setup
setup(
    name='cli-anything-aws_networkfirewall',
    version='1.0.0',
    packages=['cli_anything.aws_networkfirewall'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_networkfirewall=cli_anything.aws_networkfirewall:cli']},
)
