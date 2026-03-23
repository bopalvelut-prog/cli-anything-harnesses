from setuptools import setup
setup(
    name='cli-anything-toolbar',
    version='1.0.0',
    packages=['cli_anything.toolbar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-toolbar=cli_anything.toolbar:cli']},
)
