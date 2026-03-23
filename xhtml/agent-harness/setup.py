from setuptools import setup
setup(
    name='cli-anything-xhtml',
    version='1.0.0',
    packages=['cli_anything.xhtml'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xhtml=cli_anything.xhtml:cli']},
)
