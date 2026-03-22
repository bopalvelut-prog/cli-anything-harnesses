from setuptools import setup
setup(
    name='cli-anything-cognito',
    version='1.0.0',
    packages=['cli_anything.cognito'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cognito=cli_anything.cognito:cli']},
)
