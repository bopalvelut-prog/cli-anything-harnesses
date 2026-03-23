from setuptools import setup
setup(
    name='cli-anything-apple',
    version='1.0.0',
    packages=['cli_anything.apple'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apple=cli_anything.apple:cli']},
)
