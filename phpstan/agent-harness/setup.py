from setuptools import setup
setup(
    name='cli-anything-phpstan',
    version='1.0.0',
    packages=['cli_anything.phpstan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-phpstan=cli_anything.phpstan:cli']},
)
