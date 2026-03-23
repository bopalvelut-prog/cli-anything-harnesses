from setuptools import setup
setup(
    name='cli-anything-coveralls',
    version='1.0.0',
    packages=['cli_anything.coveralls'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coveralls=cli_anything.coveralls:cli']},
)
