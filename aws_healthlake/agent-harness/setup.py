from setuptools import setup
setup(
    name='cli-anything-aws_healthlake',
    version='1.0.0',
    packages=['cli_anything.aws_healthlake'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_healthlake=cli_anything.aws_healthlake:cli']},
)
