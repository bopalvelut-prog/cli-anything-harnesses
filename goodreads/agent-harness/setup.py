from setuptools import setup
setup(
    name='cli-anything-goodreads',
    version='1.0.0',
    packages=['cli_anything.goodreads'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-goodreads=cli_anything.goodreads:cli']},
)
