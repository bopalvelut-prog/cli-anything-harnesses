from setuptools import setup
setup(
    name='cli-anything-somewhat',
    version='1.0.0',
    packages=['cli_anything.somewhat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-somewhat=cli_anything.somewhat:cli']},
)
