from setuptools import setup
setup(
    name='cli-anything-dynamodb',
    version='1.0.0',
    packages=['cli_anything.dynamodb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dynamodb=cli_anything.dynamodb:cli']},
)
