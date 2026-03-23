from setuptools import setup
setup(
    name='cli-anything-caml',
    version='1.0.0',
    packages=['cli_anything.caml'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-caml=cli_anything.caml:cli']},
)
