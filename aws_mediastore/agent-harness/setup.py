from setuptools import setup
setup(
    name='cli-anything-aws_mediastore',
    version='1.0.0',
    packages=['cli_anything.aws_mediastore'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_mediastore=cli_anything.aws_mediastore:cli']},
)
