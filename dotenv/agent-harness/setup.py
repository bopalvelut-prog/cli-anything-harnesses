from setuptools import setup
setup(
    name='cli-anything-dotenv',
    version='1.0.0',
    packages=['cli_anything.dotenv'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dotenv=cli_anything.dotenv:cli']},
)
