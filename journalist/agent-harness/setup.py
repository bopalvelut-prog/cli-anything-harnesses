from setuptools import setup
setup(
    name='cli-anything-journalist',
    version='1.0.0',
    packages=['cli_anything.journalist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-journalist=cli_anything.journalist:cli']},
)
