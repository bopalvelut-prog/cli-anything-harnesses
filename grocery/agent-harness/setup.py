from setuptools import setup
setup(
    name='cli-anything-grocery',
    version='1.0.0',
    packages=['cli_anything.grocery'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grocery=cli_anything.grocery:cli']},
)
