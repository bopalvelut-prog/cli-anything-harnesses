from setuptools import setup
setup(
    name='cli-anything-pandoc',
    version='1.0.0',
    packages=['cli_anything.pandoc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pandoc=cli_anything.pandoc:cli']},
)
