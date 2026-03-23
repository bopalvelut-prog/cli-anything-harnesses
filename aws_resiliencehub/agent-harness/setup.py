from setuptools import setup
setup(
    name='cli-anything-aws_resiliencehub',
    version='1.0.0',
    packages=['cli_anything.aws_resiliencehub'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_resiliencehub=cli_anything.aws_resiliencehub:cli']},
)
