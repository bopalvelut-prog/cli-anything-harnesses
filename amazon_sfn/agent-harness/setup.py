from setuptools import setup
setup(
    name='cli-anything-amazon_sfn',
    version='1.0.0',
    packages=['cli_anything.amazon_sfn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_sfn=cli_anything.amazon_sfn:cli']},
)
