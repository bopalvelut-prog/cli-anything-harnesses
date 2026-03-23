from setuptools import setup
setup(
    name='cli-anything-purpose',
    version='1.0.0',
    packages=['cli_anything.purpose'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-purpose=cli_anything.purpose:cli']},
)
