from setuptools import setup
setup(
    name='cli-anything-wet',
    version='1.0.0',
    packages=['cli_anything.wet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wet=cli_anything.wet:cli']},
)
