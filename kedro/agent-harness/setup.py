from setuptools import setup
setup(
    name='cli-anything-kedro',
    version='1.0.0',
    packages=['cli_anything.kedro'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kedro=cli_anything.kedro:cli']},
)
