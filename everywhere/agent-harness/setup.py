from setuptools import setup
setup(
    name='cli-anything-everywhere',
    version='1.0.0',
    packages=['cli_anything.everywhere'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-everywhere=cli_anything.everywhere:cli']},
)
