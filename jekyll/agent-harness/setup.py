from setuptools import setup
setup(
    name='cli-anything-jekyll',
    version='1.0.0',
    packages=['cli_anything.jekyll'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jekyll=cli_anything.jekyll:cli']},
)
