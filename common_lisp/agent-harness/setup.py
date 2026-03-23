from setuptools import setup
setup(
    name='cli-anything-common_lisp',
    version='1.0.0',
    packages=['cli_anything.common_lisp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-common_lisp=cli_anything.common_lisp:cli']},
)
