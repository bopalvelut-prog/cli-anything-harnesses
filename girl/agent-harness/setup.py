from setuptools import setup
setup(
    name='cli-anything-girl',
    version='1.0.0',
    packages=['cli_anything.girl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-girl=cli_anything.girl:cli']},
)
