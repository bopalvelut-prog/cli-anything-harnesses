from setuptools import setup
setup(
    name='cli-anything-keydb',
    version='1.0.0',
    packages=['cli_anything.keydb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-keydb=cli_anything.keydb:cli']},
)
