from setuptools import setup
setup(
    name='cli-anything-maison',
    version='1.0.0',
    packages=['cli_anything.maison'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-maison=cli_anything.maison:cli']},
)
