from setuptools import setup
setup(
    name='cli-anything-aws_msk',
    version='1.0.0',
    packages=['cli_anything.aws_msk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_msk=cli_anything.aws_msk:cli']},
)
