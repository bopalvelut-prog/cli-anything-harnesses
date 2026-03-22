from setuptools import setup
setup(
    name='cli-anything-laravel',
    version='1.0.0',
    packages=['cli_anything.laravel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-laravel=cli_anything.laravel:cli']},
)
