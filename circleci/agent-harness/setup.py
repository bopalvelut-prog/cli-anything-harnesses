from setuptools import setup
setup(
    name='cli-anything-circleci',
    version='1.0.0',
    packages=['cli_anything.circleci'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-circleci=cli_anything.circleci:cli']},
)
