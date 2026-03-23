from setuptools import setup
setup(
    name='cli-anything-reader',
    version='1.0.0',
    packages=['cli_anything.reader'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reader=cli_anything.reader:cli']},
)
