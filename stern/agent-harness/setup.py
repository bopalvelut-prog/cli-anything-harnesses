from setuptools import setup
setup(
    name='cli-anything-stern',
    version='1.0.0',
    packages=['cli_anything.stern'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stern=cli_anything.stern:cli']},
)
