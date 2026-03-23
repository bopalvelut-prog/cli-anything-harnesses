from setuptools import setup
setup(
    name='cli-anything-neck',
    version='1.0.0',
    packages=['cli_anything.neck'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-neck=cli_anything.neck:cli']},
)
