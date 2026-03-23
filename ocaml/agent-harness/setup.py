from setuptools import setup
setup(
    name='cli-anything-ocaml',
    version='1.0.0',
    packages=['cli_anything.ocaml'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ocaml=cli_anything.ocaml:cli']},
)
