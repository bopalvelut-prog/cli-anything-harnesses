from setuptools import setup
setup(
    name='cli-anything-decimal',
    version='1.0.0',
    packages=['cli_anything.decimal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-decimal=cli_anything.decimal:cli']},
)
