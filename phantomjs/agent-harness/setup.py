from setuptools import setup
setup(
    name='cli-anything-phantomjs',
    version='1.0.0',
    packages=['cli_anything.phantomjs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-phantomjs=cli_anything.phantomjs:cli']},
)
