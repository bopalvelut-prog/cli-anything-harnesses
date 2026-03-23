from setuptools import setup
setup(
    name='cli-anything-rxjava',
    version='1.0.0',
    packages=['cli_anything.rxjava'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rxjava=cli_anything.rxjava:cli']},
)
