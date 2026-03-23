from setuptools import setup
setup(
    name='cli-anything-pastebin',
    version='1.0.0',
    packages=['cli_anything.pastebin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pastebin=cli_anything.pastebin:cli']},
)
