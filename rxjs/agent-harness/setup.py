from setuptools import setup
setup(
    name='cli-anything-rxjs',
    version='1.0.0',
    packages=['cli_anything.rxjs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rxjs=cli_anything.rxjs:cli']},
)
