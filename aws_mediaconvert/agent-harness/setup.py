from setuptools import setup
setup(
    name='cli-anything-aws_mediaconvert',
    version='1.0.0',
    packages=['cli_anything.aws_mediaconvert'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_mediaconvert=cli_anything.aws_mediaconvert:cli']},
)
