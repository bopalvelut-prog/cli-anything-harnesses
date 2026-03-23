from setuptools import setup
setup(
    name='cli-anything-quantlib',
    version='1.0.0',
    packages=['cli_anything.quantlib'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quantlib=cli_anything.quantlib:cli']},
)
