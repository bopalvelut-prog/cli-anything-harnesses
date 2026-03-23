from setuptools import setup
setup(
    name='cli-anything-future',
    version='1.0.0',
    packages=['cli_anything.future'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-future=cli_anything.future:cli']},
)
