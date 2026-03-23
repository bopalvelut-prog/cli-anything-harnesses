from setuptools import setup
setup(
    name='cli-anything-aws_mediapackage',
    version='1.0.0',
    packages=['cli_anything.aws_mediapackage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_mediapackage=cli_anything.aws_mediapackage:cli']},
)
