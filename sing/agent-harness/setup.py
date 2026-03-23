from setuptools import setup
setup(
    name='cli-anything-sing',
    version='1.0.0',
    packages=['cli_anything.sing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sing=cli_anything.sing:cli']},
)
