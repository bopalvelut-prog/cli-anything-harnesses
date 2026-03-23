from setuptools import setup
setup(
    name='cli-anything-desire',
    version='1.0.0',
    packages=['cli_anything.desire'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-desire=cli_anything.desire:cli']},
)
