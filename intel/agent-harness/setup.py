from setuptools import setup
setup(
    name='cli-anything-intel',
    version='1.0.0',
    packages=['cli_anything.intel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-intel=cli_anything.intel:cli']},
)
