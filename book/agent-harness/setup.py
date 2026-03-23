from setuptools import setup
setup(
    name='cli-anything-book',
    version='1.0.0',
    packages=['cli_anything.book'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-book=cli_anything.book:cli']},
)
