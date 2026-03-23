from setuptools import setup
setup(
    name='cli-anything-url',
    version='1.0.0',
    packages=['cli_anything.url'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-url=cli_anything.url:cli']},
)
