from setuptools import setup
setup(
    name='cli-anything-previous',
    version='1.0.0',
    packages=['cli_anything.previous'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-previous=cli_anything.previous:cli']},
)
