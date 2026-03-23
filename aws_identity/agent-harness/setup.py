from setuptools import setup
setup(
    name='cli-anything-aws_identity',
    version='1.0.0',
    packages=['cli_anything.aws_identity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_identity=cli_anything.aws_identity:cli']},
)
