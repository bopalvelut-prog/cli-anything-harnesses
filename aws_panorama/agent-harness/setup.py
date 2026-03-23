from setuptools import setup
setup(
    name='cli-anything-aws_panorama',
    version='1.0.0',
    packages=['cli_anything.aws_panorama'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_panorama=cli_anything.aws_panorama:cli']},
)
