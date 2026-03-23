from setuptools import setup
setup(
    name='cli-anything-framadate',
    version='1.0.0',
    packages=['cli_anything.framadate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-framadate=cli_anything.framadate:cli']},
)
