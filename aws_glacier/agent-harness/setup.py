from setuptools import setup
setup(
    name='cli-anything-aws_glacier',
    version='1.0.0',
    packages=['cli_anything.aws_glacier'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_glacier=cli_anything.aws_glacier:cli']},
)
