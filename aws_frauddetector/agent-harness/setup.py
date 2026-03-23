from setuptools import setup
setup(
    name='cli-anything-aws_frauddetector',
    version='1.0.0',
    packages=['cli_anything.aws_frauddetector'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_frauddetector=cli_anything.aws_frauddetector:cli']},
)
