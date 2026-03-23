from setuptools import setup
setup(
    name='cli-anything-expressjs',
    version='1.0.0',
    packages=['cli_anything.expressjs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-expressjs=cli_anything.expressjs:cli']},
)
