from setuptools import setup
setup(
    name='cli-anything-happen',
    version='1.0.0',
    packages=['cli_anything.happen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-happen=cli_anything.happen:cli']},
)
