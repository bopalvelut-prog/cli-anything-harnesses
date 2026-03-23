from setuptools import setup
setup(
    name='cli-anything-aws_mediatailor',
    version='1.0.0',
    packages=['cli_anything.aws_mediatailor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_mediatailor=cli_anything.aws_mediatailor:cli']},
)
