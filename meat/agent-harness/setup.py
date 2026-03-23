from setuptools import setup
setup(
    name='cli-anything-meat',
    version='1.0.0',
    packages=['cli_anything.meat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-meat=cli_anything.meat:cli']},
)
