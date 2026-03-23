from setuptools import setup
setup(
    name='cli-anything-amazon_bedrock',
    version='1.0.0',
    packages=['cli_anything.amazon_bedrock'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_bedrock=cli_anything.amazon_bedrock:cli']},
)
