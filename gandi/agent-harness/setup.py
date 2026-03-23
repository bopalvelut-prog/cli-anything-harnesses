from setuptools import setup
setup(
    name='cli-anything-gandi',
    version='1.0.0',
    packages=['cli_anything.gandi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gandi=cli_anything.gandi:cli']},
)
