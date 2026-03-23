from setuptools import setup
setup(
    name='cli-anything-matter',
    version='1.0.0',
    packages=['cli_anything.matter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-matter=cli_anything.matter:cli']},
)
