from setuptools import setup
setup(
    name='cli-anything-aws_fis',
    version='1.0.0',
    packages=['cli_anything.aws_fis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_fis=cli_anything.aws_fis:cli']},
)
