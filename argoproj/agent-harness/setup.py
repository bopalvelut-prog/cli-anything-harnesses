from setuptools import setup
setup(
    name='cli-anything-argoproj',
    version='1.0.0',
    packages=['cli_anything.argoproj'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-argoproj=cli_anything.argoproj:cli']},
)
