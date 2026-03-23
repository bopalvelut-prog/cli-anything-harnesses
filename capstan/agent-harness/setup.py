from setuptools import setup
setup(
    name='cli-anything-capstan',
    version='1.0.0',
    packages=['cli_anything.capstan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-capstan=cli_anything.capstan:cli']},
)
