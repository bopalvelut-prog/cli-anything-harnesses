from setuptools import setup
setup(
    name='cli-anything-lambda',
    version='1.0.0',
    packages=['cli_anything.lambda'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lambda=cli_anything.lambda:cli']},
)
