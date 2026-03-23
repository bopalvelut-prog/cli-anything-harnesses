from setuptools import setup
setup(
    name='cli-anything-escape',
    version='1.0.0',
    packages=['cli_anything.escape'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-escape=cli_anything.escape:cli']},
)
