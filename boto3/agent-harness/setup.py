from setuptools import setup
setup(
    name='cli-anything-boto3',
    version='1.0.0',
    packages=['cli_anything.boto3'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-boto3=cli_anything.boto3:cli']},
)
